#!/usr/bin/env python3

import argparse
import csv

from dobishem.storage import read_csv

import pydot

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--title", "-t",
        help="""The title of the chart.""")
    parser.add_argument(
        "--graph-type", "-g",
        default='digraph',
        help="""The graph type to produce.""")
    parser.add_argument(
        "--rankdir", "-r",
        default='TB',
        help="""The rank direction to use.""")
    parser.add_argument(
        "--links", "-l",
        help="""The name of the file containing the links.
        Each row should have three elements: origin, type, destination.
        The first row is skipped, treating it as a header.""")
    parser.add_argument(
        "--details", "-d",
        help="""The name of the file containing node details.""")
    parser.add_argument(
        "--node-key-column", "-k", default='name',
        help="""The name of the column in the node details file to use as node keys.""")
    parser.add_argument(
        "--node-style-column", "-S", default='style',
        help="""The name of the column to use as node styles.
        Node styles are looked up in the style table.""")
    parser.add_argument(
        "--style", "-s",
        help="""The name of the file containing the style table.
        Each row should have a 'Style' cell which names the style.
        Other cells in the row should be named as the options to
        pydot's constructors.""")
    # parser.add_argument(
    #     "--node-shape",
    #     default='box',
    #     help="""The shape to use for nodes.""")
    parser.add_argument(
        "--output", "-o",
        help="""The name of the output file.""")
    return vars(parser.parse_args())

def charter(title,
            nodes,
            links,
            styles,
            node_style_column,
            **kwargs):
    graph = pydot.Dot(title,
                      **kwargs)
    for name, node in nodes.items():
        graph.add_node(pydot.Node(name,
                                  **styles.get(node[node_style_column],
                                               {})))
    for source, linktype, destination in links:
        graph.add_edge(pydot.Edge(source, destination,
                                  **styles.get(linktype,
                                               {})))
    return graph

def charter_main(details,
                 node_key_column,
                 node_style_column,
                 links,
                 style,
                 title,
                 output,
                 # node_shape,
                 **kwargs):
    result = charter(title=title,
                     links=read_csv(links,
                                    result_type=list,
                                    row_type=list)[1:],
                     nodes=read_csv(details,
                                    result_type=dict,
                                    key_column=node_key_column),
                     styles=read_csv(style,
                                     result_type=dict,
                                     key_column='Style',
                                     strip_key=True,
                                     remove_blanks=True,
                                     row_type=dict),
                     node_style_column=node_style_column,
                     **kwargs)
    if output.endswith(".png"):
        result.write_png(output)
    else:
        with open(output, 'w') as outstream:
            outstream.write(result.to_string())

if __name__ == "__main__":
    charter_main(**get_args())
