# DEPRECATED: Service Scripts

Scripts to handle some pre-processing of data for the site.
_These are kept for reference only, as we know turned back to manually maintained master
file formatted in YAML_.

## Collaboration membership

The script 'people.py' produces a file containing the list of active members,
named 'collaboration.csv' which should be copied to the folder '_data'.

It takes the following arguments which are filenames of the files extracted from the PHENIX official DB:
- members in good standing
- institutions
- affiliations
- email addresses
- general list of the whole collaboration
