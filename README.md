MOENCHImageCounterController
===============
It is not possible to save both the image (returned from `ReadOne`) and the reference (returned from `RefOne`) in the current version (see [issue](https://gitlab.com/sardana-org/sardana/-/issues/1738#note_920602318)).

However, it is possible to retrieve an image within a measurement group via `ReadOne`. Thus, in order to be able to 
not only the reference but also a preview of the image in the `.h5` file, it is necessary to read out and return the image in this `PseudoCounterController`.