from zope.interface import Interface as I

from bit.content.graphic.interfaces\
    import IGraphical, IIconic

from plone.indexer.decorator import indexer


@indexer(I)
def getIcon(obj, **kwa):
    graphical = IGraphical(obj, None)
    icon = ''
    if graphical:
        icon = graphical.get_graphic('icon')
    if not icon:
        iconic = IIconic(obj, None)
        if iconic:
            icon = iconic.get_icon()
    if not icon:
        icon = obj.getIcon(True)
    return icon


@indexer(I)
def getGraphics(obj, **kwa):
    graphical = IGraphical(obj, None)
    return graphical and graphical.graphic_list()


@indexer(I)
def getThumbnail(obj, **kwargs):
    graphical = IGraphical(obj, None)
    return graphical and graphical.get_graphic('thumb') or None
