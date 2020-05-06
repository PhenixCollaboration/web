---
abbrev: acc
layout: newbase
category: central
---

{% include layouts/find_detector_title.md abbrev=page.abbrev %}
# {{ title }}

#### Aerogel overview

The Aerogel is a Cherenkov counter detector.  It comprises 160 boxes, each with 2
photomultiplier tubes for a total of 320 channels.  Each box is filled with aerogel
material with an index of refraction of n = 1.0113.  It occupies the full acceptance of
sector 1 in the west arm.



#### Aerogel analysis variables

{% include layouts/variables.md rows=site.data.acc.vars %}

<br>

Unlike most central arm detectors, the Aerogel variables are not accessible directly from
`PHCentralTrack` or `PHSnglCentralTrack` but instead are accessed from their own classes
`AccCluster` and `AccSnglCluster`.  There are very few Aerogel variables, so we present
all of them here in the form of an analysis code snippet to simultaneously illustrate how
to get them and what they are.


```c++
  PHCentralTrack* d_cnt = getClass<PHCentralTrack>(topNode,"PHCentralTrack");
  AccCluster* d_acccl = getClass<AccCluster>(topNode,"AccCluster");
  for ( unsigned int itrk = 0; itrk < d_cnt->get_npart(); ++itrk )
    {
      // get the aerogel cluster index for this track either
      // from PHCentralTrack or PHSnglCentralTrack
      int aerindex = d_cnt->get_aerindex(itrk);

      // get the single cluster object from the cluster container
      // using the cluster index
      AccSnglCluster* d_clus = d_acccl->get_cluster(aerindex);

      // get the global box number of the hit from the single cluster object
      int aerhitid = d_clus->get_aerhitid();

      // get the local box number of the hit from the single cluster object
      int aerhitconfig = d_clus->get_aerhitconfig();

      // get the variables using the local box number

      // number of photoelectrons in PMT1
      float aerph1 = d_clus->get_aerph1(aerhitconfig);
      // number of photoelectrons in PMT2
      float aerph2 = d_clus->get_aerph2(aerhitconfig);
      // time of PMT1
      float aert1 = d_clus->get_aert1(aerhitconfig);
      // time of PMT2
      float aert2 = d_clus->get_aert2(aerhitconfig);
    }
```

