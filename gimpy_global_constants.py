GRAPH_ATTRIBUTES = set( ['Damping', 'K', 'URL', 'aspect', 'bb', 'bgcolor',
    'center', 'charset', 'clusterrank', 'colorscheme', 'comment', 'compound',
    'concentrate', 'defaultdist', 'dim', 'dimen', 'diredgeconstraints',
    'dpi', 'epsilon', 'esep', 'fontcolor', 'fontname', 'fontnames',
    'fontpath', 'fontsize', 'id', 'label', 'labeljust', 'labelloc',
    'landscape', 'layers', 'layersep', 'layout', 'levels', 'levelsgap',
    'lheight', 'lp', 'lwidth', 'margin', 'maxiter', 'mclimit', 'mindist',
    'mode', 'model', 'mosek', 'nodesep', 'nojustify', 'normalize', 'nslimit',
    'nslimit1', 'ordering', 'orientation', 'outputorder', 'overlap',
    'overlap_scaling', 'pack', 'packmode', 'pad', 'page', 'pagedir',
    'quadtree', 'quantum', 'rankdir', 'ranksep', 'ratio', 'remincross',
    'repulsiveforce', 'resolution', 'root', 'rotate', 'searchsize', 'sep',
    'showboxes', 'size', 'smoothing', 'sortv', 'splines', 'start', 
    'stylesheet', 'target', 'truecolor', 'viewport', 'voro_margin',
    # for subgraphs 
    'rank'])
DEFAULT_GRAPH_ATTRIBUTES = {}
EDGE_ATTRIBUTES = set( ['URL', 'arrowhead', 'arrowsize', 'arrowtail',
    'color', 'colorscheme', 'comment', 'constraint', 'decorate', 'dir',
    'edgeURL', 'edgehref', 'edgetarget', 'edgetooltip', 'fontcolor',
    'fontname', 'fontsize', 'headURL', 'headclip', 'headhref', 'headlabel',
    'headport', 'headtarget', 'headtooltip', 'href', 'id', 'label',
    'labelURL', 'labelangle', 'labeldistance', 'labelfloat', 'labelfontcolor',
    'labelfontname', 'labelfontsize', 'labelhref', 'labeltarget',
    'labeltooltip', 'layer', 'len', 'lhead', 'lp', 'ltail', 'minlen',
    'nojustify', 'penwidth', 'pos', 'samehead', 'sametail', 'showboxes',
    'style', 'tailURL', 'tailclip', 'tailhref', 'taillabel', 'tailport',
    'tailtarget', 'tailtooltip', 'target', 'tooltip', 'weight',
    'rank' ] )
DEFAULT_EDGE_ATTRIBUTES = {}
NODE_ATTRIBUTES = set( ['URL', 'color', 'colorscheme', 'comment',
    'distortion', 'fillcolor', 'fixedsize', 'fontcolor', 'fontname',
    'fontsize', 'group', 'height', 'id', 'image', 'imagescale', 'label',
    'labelloc', 'layer', 'margin', 'nojustify', 'orientation', 'penwidth',
    'peripheries', 'pin', 'pos', 'rects', 'regular', 'root', 'samplepoints',
    'shape', 'shapefile', 'showboxes', 'sides', 'skew', 'sortv', 'style',
    'target', 'tooltip', 'vertices', 'width', 'z',
    # The following are attributes dot2tex
    'texlbl',  'texmode' ] )
DEFAULT_NODE_ATTRIBUTES = {}
CLUSTER_ATTRIBUTES = set( ['K', 'URL', 'bgcolor', 'color', 'colorscheme',
    'fillcolor', 'fontcolor', 'fontname', 'fontsize', 'label', 'labeljust',
    'labelloc', 'lheight', 'lp', 'lwidth', 'nojustify', 'pencolor',
    'penwidth', 'peripheries', 'sortv', 'style', 'target', 'tooltip'] )
DIRECTED_GRAPH = 'digraph'
UNDIRECTED_GRAPH = 'graph'
#DEFAULT_ATTR = {'strict':None, 'name':'graph'}
EDGE_CONNECT_SYMBOL = {DIRECTED_GRAPH:' -> ', UNDIRECTED_GRAPH:' -- '}
