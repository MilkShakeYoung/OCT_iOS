{{TOC}}

# OCT_iOS
OCT, which is [optical coherence tomography](https://en.wikipedia.org/wiki/Optical_coherence_tomography), can be used for detecting retina in micron resolution.Now we can obtain OCT signal by [Pythonista](http://omz-software.com/pythonista/) in iOS devices.
## Steps

1. Get access token from Dropbox by ```DropboxFileGet.py```, and files in target folders could be downloaded to root folder in Pythonista
2. The interference signal example is ```NKT_15us_3thou.csv```. Run ```FFT_iOS.py```with file ```NKT_15us_3thou.csv```
3. ```A-scan Signal.PNG``` can be shown in Pythonista console.
