---
layout: newbase
name: archive
---
##### The current plots database
###### Query link
https://phenix-intra.sdcc.bnl.gov/WWW/plots/search_plots.php
<hr/>
###### Plots
```
              Table "public.plots"
   Column    |         Type          | Modifiers 
-------------+-----------------------+-----------
 plotid      | character varying(30) | not null
 predir      | text                  | 
 filecnt     | integer               | 
 nameid      | integer               | 
 speaker     | integer               | 
 confid      | character varying(30) | 
 approvename | integer               | 
 submitdate  | date                  | 
 approvedate | date                  | 
 releasedate | date                  | 
 status      | character varying(30) | 
 title       | text                  | 
 publink     | text                  | 
 theocurves  | text                  | 
 otherdata   | text                  | 
 summary     | text                  | 
 comment     | text                  | 
 entry       | integer               | not null
 archive     | character varying(10) | 
 public_tag  | character varying(10) | 
Indexes:
    "plots_pkey" PRIMARY KEY, btree (entry)
    "plots_plotid_key" UNIQUE CONSTRAINT, btree (plotid)
Foreign-key constraints:
    "plots_approvename_fkey" FOREIGN KEY (approvename) REFERENCES people(id)
    "plots_confid_fkey" FOREIGN KEY (confid) REFERENCES phnxconf2(confid)
    "plots_nameid_fkey" FOREIGN KEY (nameid) REFERENCES people(id)
    "plots_speaker_fkey" FOREIGN KEY (speaker) REFERENCES people(id)
Referenced by:
    TABLE "plot_cs_run" CONSTRAINT "plot_cs_run_plot_num_fkey" FOREIGN KEY (plot_num) REFERENCES plots(entry)
    TABLE "plot_pwg" CONSTRAINT "plot_pwg_plot_num_fkey" FOREIGN KEY (plot_num) REFERENCES plots(entry)
    TABLE "plot_rel_pub" CONSTRAINT "plot_rel_pub_plot_num_fkey" FOREIGN KEY (plot_num) REFERENCES plots(entry)
    TABLE "plot_sp_type" CONSTRAINT "plot_sp_type_plot_num_fkey" FOREIGN KEY (plot_num) REFERENCES plots(entry)
    TABLE "plot_xcol" CONSTRAINT "plot_xcol_plot_num_fkey" FOREIGN KEY (plot_num) REFERENCES plots(entry)
    TABLE "plot_ycol" CONSTRAINT "plot_ycol_plot_num_fkey" FOREIGN KEY (plot_num) REFERENCES plots(entry)
    TABLE "plotfiles" CONSTRAINT "plotfiles_plot_num_fkey" FOREIGN KEY (plot_num) REFERENCES plots(entry)
```
<hr/>
###### plot_xcol, plot_x_axis
```
Table "public.plot_xcol"
  Column  |  Type   | Modifiers 
----------+---------+-----------
 plot_num | integer | not null
 xid      | integer | not null
Indexes:
    "plot_xcol_pkey" PRIMARY KEY, btree (plot_num, xid)
Foreign-key constraints:
    "plot_xcol_plot_num_fkey" FOREIGN KEY (plot_num) REFERENCES plots(entry)
    "plot_xcol_xid_fkey" FOREIGN KEY (xid) REFERENCES plot_x_axis(id)

phenix_collab=# \d plot_x_axis;
    Table "public.plot_x_axis"
   Column    |  Type   | Modifiers 
-------------+---------+-----------
 id          | integer | not null
 name        | text    | 
 description | text    | 
Indexes:
    "plot_x_axis_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "plot_xcol" CONSTRAINT "plot_xcol_xid_fkey" FOREIGN KEY (xid) REFERENCES plot_x_axis(id)
```
