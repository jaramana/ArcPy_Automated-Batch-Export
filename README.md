# Automated Batch Export

**Project Description**

Many times when I am tasked with mapping projects, a lot of time and effort is spent toggling layers and bookmarks to export individually, only to then wait for the export to finish to repeat the process, over and over again. The goal of this project is to automate this process as much as possible.

**How to Use**

1. Fill in all the desired bookmarks, layers, and export destination
2. Run
3. The exports should appear in their destination folder

**Python Dependencies**

-arcpy

**Current Limitations**


Having difficulty clearing the layers I enabled previously for the next export. I tried using the '''else:''' function, but I kept receiving errors. I tried all the indentations I thought possible and ordered them in different ways to no avail.

My workaround is to use the '''del mxd''' function and just re-input the mxd after each export. I imagine this will slow things down, but it works.

The script could also use some cleaning to make it more compact and easier to use if there were many exports (think 20+).


**Specific Project Examples**

At the moment, I am working on a project that studies Public Investment and their relationship to different community districts in New York City.

We've identified a series of variables and topics that could potentially be interesting in this study, and I am tasked with mapping and visualizing them.

_Some of them include:_

* Community Facilities
    * Parks and Open Spaces
    * Schools
    * Public Library
    * LinkNYC and Public WiFi
* <b>Transportation</b>
    * Bicycle
    * Subway
    * <b>Bus</b>
    * Ferry Routes
* Housing
    * Building by Year Built
    * Inclusionary Housing Area
    * 421-a Tax Lots
    * NYCHA Properties


This script should relieve the challenge of continuous layer toggling and changing bookmarks/extents. This process would usually be painstakingly long and cumbersome if using the ArcMap user interface.

For example, I will just be showing the Bus, in the Transportation category, and will only be exporting extents from two bookmarks.


**Pseudocode for example**
```
import arcpy

mxd = arcpy.mapping.MapDocument(r"C:\Users\USER\Documents\GIS\AIA_1.mxd")
layers = arcpy.mapping.ListLayers(mxd, "*")
for bkmk in arcpy.mapping.ListBookmarks(mxd, "CD103"):
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext
    for item in layers:
        if item.name == 'Basemap and Boundaries':
            item.visible = True
        if item.name == 'Mask':
            item.visible = True
        if item.name == 'Transportation':
            item.visible = True
        if item.name == 'Bus':
            item.visible = True
        if item.name == 'Bus Routes SBS':
            item.visible = True
        if item.name == 'Bus Routes':
            item.visible = True
    arcpy.mapping.overwriteOutput = True
    arcpy.mapping.ExportToPNG(mxd, r"C:\Users\USER\Documents\Exports\Bus CD103".format(bkmk.name),resolution=100)
del mxd

mxd = arcpy.mapping.MapDocument(r"C:\Users\USER\Documents\GIS\AIA_1.mxd")
layers = arcpy.mapping.ListLayers(mxd, "*")
for bkmk in arcpy.mapping.ListBookmarks(mxd, "CD201"):
    ext = bkmk.extent
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.extent = ext
    for item in layers:
        if item.name == 'Basemap and Boundaries':
            item.visible = True
        if item.name == 'Mask':
            item.visible = True
        if item.name == 'Transportation':
            item.visible = True
        if item.name == 'Bus':
            item.visible = True
        if item.name == 'Bus Routes SBS':
            item.visible = True
        if item.name == 'Bus Routes':
            item.visible = True
    arcpy.mapping.overwriteOutput = True
    arcpy.mapping.ExportToPNG(mxd, r"C:\Users\USER\Documents\Exports\Bus CD201".format(bkmk.name),resolution=100)
del mxd

```

**Standardized Psuedocode**
```
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
```
