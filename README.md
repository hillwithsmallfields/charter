# charter
Most charters define organizations.  This one makes charts.

Usage:

    charter.py [--title TITLE] --links LINKS --details DETAILS [--node-key-column NODE_KEY_COLUMN] [--node-style-column NODE_STYLE_COLUMN] --style STYLE --output OUTPUT

Options:

`--title TITLE, -t TITLE`

The title of the chart.

`--links LINKS, -l LINKS`

The name of the file containing the links. Each row should have three elements: origin, type, destination. The first row is skipped, treating it as a header.

`--details DETAILS, -d DETAILS`

The name of the file containing node details.

`--node-key-column NODE_KEY_COLUMN, -k NODE_KEY_COLUMN`

The name of the column in the node details file to use as node keys.

`--node-style-column NODE_STYLE_COLUMN, -S NODE_STYLE_COLUMN`

The name of the column to use as node styles. Node styles are looked up in the style table.

`--style STYLE, -s STYLE`

The name of the file containing the style table. Each row should have a 'Style' cell which names the style. Other cells in the row should be named as the options to pydot's constructors.

`--output OUTPUT, -o OUTPUT`

The name of the output file.
