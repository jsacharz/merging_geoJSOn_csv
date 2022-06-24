# merging_geoJSOn_csv

### Intro: Combining geoJASON data and other quantitive data is the very first step of data wrangling when setting up Leaflet.js and Chloropleth. 
However, merging geoJSOn with other type of files can be tricky. Often programs such QGIS allow to perform such operation between two sets of data with equal numbers of rows in the sources data. 

Data samples: 

(1) geoJSON: 2979 rows, coordinates for polygon, name of the suburb - used to draw the boundry in the map

(2) cleaned cvs: 297 rows with suburs names (primey key) and sales values - used to assing the gradeint colour in Chloropleth

This Python script allows to combine geoJSON data with quantititve data which can then be used for Leaflet and Chlorpleth.
