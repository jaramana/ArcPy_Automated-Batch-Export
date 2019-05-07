# import modules
import arcpy

# EXPORT 1
# set the  mxd
mxd = arcpy.mapping.MapDocument(r"DESTINATION TO MXD")
# import layers
layers = arcpy.mapping.ListLayers(mxd, "*")
# import bookmarks and define desired bookmark
for bkmk in arcpy.mapping.ListBookmarks(mxd, "BOOKMARK X"):
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext
    for item in layers:
        # input the desired layers to be toggled on
        if item.name == 'LAYER X':
            item.visible = True
        if item.name == 'LAYER X':
            item.visible = True
    # overwrite exports
    arcpy.mapping.overwriteOutput = True
    # output and export destination and characteristics
    arcpy.mapping.ExportToPNG(mxd, r"PATH TO EXPORT DESTINATION".format(bkmk.name))
del mxd


# EXPORT 2
mxd = arcpy.mapping.MapDocument(r"DESTINATION TO MXD")
layers = arcpy.mapping.ListLayers(mxd, "*")
for bkmk in arcpy.mapping.ListBookmarks(mxd, "BOOKMARK X"):
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext
    for item in layers:
        if item.name == 'LAYER X':
            item.visible = True
        if item.name == 'LAYER X':
            item.visible = True
    arcpy.mapping.overwriteOutput = True
    arcpy.mapping.ExportToPNG(mxd, r"PATH TO EXPORT DESTINATION".format(bkmk.name))
del mxd


# EXPORT 3
mxd = arcpy.mapping.MapDocument(r"DESTINATION TO MXD")
layers = arcpy.mapping.ListLayers(mxd, "*")
for bkmk in arcpy.mapping.ListBookmarks(mxd, "BOOKMARK X"):
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext
    for item in layers:
        if item.name == 'LAYER X':
            item.visible = True
        if item.name == 'LAYER X':
            item.visible = True
    arcpy.mapping.overwriteOutput = True
    arcpy.mapping.ExportToPNG(mxd, r"PATH TO EXPORT DESTINATION".format(bkmk.name))
del mxd
