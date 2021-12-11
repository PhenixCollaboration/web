---
name: custom_components
layout: newbase
---

<h3>Custom Components used in PHENIX analysis macros</h3>

* TOC
{:toc}

---

#### THmulf

##### Overview
The ```THmulf``` C++ class was created to increase the efficiency of the
analysis ROOT macros used in PHENIX analyses.
Specifically, the class was written to provide the compactness of the histogram
with the ability to apply selection criteria when projecting or
drawing from it.

*THmulf sparse histograms were important before ROOT implemented its own sparse histograms with arbitrary dimensions called
[THnSparse](http://root.cern.ch/root/html/THnSparse.html){:target="_blank"}.
Please consider using THnSparse instead of THmulf, since THmulf has some surprising behavior and is not updated anymore.*

##### Quick Start Guide

To compile a macro that contains THMulfs on the commandline:
```c++
 gSystem->AddIncludePath("-I${OFFLINE_MAIN}/include"); // In order to find THMulf.h
 gSystem->Load("libTHmul.so"); // In order to load the code for the class, including the dictionary
 ```

It helps if ```$OFFLINE_MAIN/lib``` is in your ```LD_LIBRARY_PATH```.

##### Reference

Here is a list of the most commonly used calls to the ```THmulf``` interface.

###### Constructors

Create a THmulf - at this point it has no axes.

```c++
THmulf::THmulf();
THmulf::THmulf(const char* name, const char* title);
```



###### Add an axis with fixed-width bins

```c++
bool AddAxis(const char* name, const char* title, int nbins, float low, float up);
```
###### Add an axis with variable-width bins

```c++
bool AddAxis(const char* name, const char* title, int nbins, double* lowedges);
```

###### Add an axis from an already existing axis

```c++
bool AddAxis(TAxis* axis);
```

###### Add all axes from a THmulf to this THmulf

```c++
bool AddAxis(THmulf* th);
```

###### Fill a bin with a weigth w

```c++
int Fill(float w, float x0, float x1 = 0, float x2 = 0, float x3 = 0, float x4 = 0, float x5 = 0, float x6 = 0, 
float x7 = 0, float x8 = 0, float x9 = 0, float x10 = 0, float x11 = 0, float x12 = 0, float x13 = 0);
```

*Can be used up to 14 dimensions.*

###### Add c1*th to this object

```c++
bool Add(THmulf* th, double c1 = 1);
```

###### Make a topological comparison between two THmulfs

```c++
static int CompareTopology(THmulf& a, THmulf& b, int verbose=0);
```

*Returns 0 if they are the "same" (Can be useful before Add-ing).*

---

##### THmulf Example

Storing and plotting some particle properties.
As we would like to spare disk space, and don't mind some granularity,
a Thmulf is the ideal choice.
Note that the access time increases heavily with the number of axes and bins.

So, when initializing our code (eg. in MyFun4AllModule::Init), create our multi-dimensonal histogram.
```c++
th = new THmulf("th","emcal mass");
th->AddAxis("tof","tof",128,-16,16);
th->AddAxis("sector","sector",8,-0.5,7.5);
th->AddAxis("e","e",20,0,2);
th->AddAxis("cm","charge*momentum",120,-3,3);
```

Optionally register it with Fun4AllHistoManager,
so that we can use the standard way of saving it.

Fill it up in the data-processing loop (usually in process_event).
Here we specify the same (1.0) weight weight for every entry.

```c++
th->Fill(1.0, cluster->tof(), sector, cluster->e(), track->get_charge()*track->get_mom())
```

When done, you can save it using the ROOT or the Fun4All way. Then retreive it as you would get any other histogram.

The great thing in THmulf is that you can treat it as if it were a TTree, that you are probably used to. Let's plot the photon time peak in W0:

```c++
th->Draw("tof","abs(e/mom - 1.0)<0.2&&sector==0");
```

Just as by TTrees, we can save this into a 1d histo TH1F * h at the same time:
```c++
TH1F * h = new TH1F("h","photon time of flight",128,-16,16);
th->Draw("tof>>h","abs(e/mom - 1.0)<0.2&&sector==0");
```

#### haddPhenix

There is a utility which is modified from the root ```hadd``` program, *haddPhenix* which you can use to add THmulf's from different files:
```bash
haddPhenix newfile.root orig1.root orig2.root orig3.root
```