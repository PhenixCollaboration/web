---
name: reana
layout: newbase
---
{% include layouts/find_title.md name=page.name %}

##### Overview
{% include navigation/findlink.md name='reana' tag='REANA' %}
is a reproducible research data analysis *platform* developed at CERN.
It is considered for Analysis Preservation in PHENIX due to the following features:

* Unambiguous description of workflows (encoded in YAML)
* Capture and preservation of both the software and the software environment by using **containerization**

REANA workflows can be represented as *Directed Acyclic Graphs* which is reflected in
the YAML schema based on the 
{% include navigation/findlink.md name='cwl' tag='Common Workflow Language (CWL)' -%}.
Each computational component of a workflow *may* require a separate and distinct
{% include navigation/pagelink.md folder=site.analysis name='docker' tag='Docker container' -%},
although individual steps can be as simple as a shell command writing a comment to a log file,
in which case containers would be redundant.

Execution of workflows in REANA requires a properly configured **REANA cluster**.
One such cluster is available to CERN users, and there are instances at other
institutions. There is also a test instance currently being evaluated at BNL
and it is available on the internal BNL network only. *Access to REANA clusters
is controlled by their administrators granting access tokens to qualified users*.
The user interacts with a REANA cluster via its network
interface (HTTPS), either via the Web GUI for a quick overview of workflows
in various stages of execution, or the CLI client which affords the user
full access to all REANA functions. The client also makes it possible to
use an automated agent for interaction with the system by scripting various
actions.

##### The Token
To be able to access a REANA cluster the user must first establish an account
by choosing the "sign up" option in the Web interface. Each user must be approved
by the system administrator, and in case of BNL having a valid SDCC account is
a prerequisite for such approval. Once an account is created, it becomes possible
to log in and the user can obtain their REANA *access token* in the profile section
in the upper right corner of the REANA web page.

by the administrators (this may be specific to each institution hosting its REANA
facility and typically involves visiting the requisite Web page). 

##### REANA Client
To user the REANA system, client software must be installed on the user's machine.
It is Python-based and at the time of writing Python 3.6 and higher is recommended.
This is often done via the Python "virtual environment" mechanism. If the "virtualenv"
tools is available the following example will work:
```bash
# Assuming the user runs "bash" on their personal machine:
# Create new virtual environment
cd
mkdir .virtualenvs # the exact name is unimportant
virtualenv ~/.virtualenvs/reana # "reana" folder can be named differently as well, as long as its use is consistent
source ~/.virtualenvs/reana/bin/activate # a self-contained Python environment is now available
# Install reana-client
pip install reana-client # installation takes place within the virtual environment
```
Alternatively, if "virtualenv" is not available (such is the case on the interactive SDCC
nodes) a slightly different method may be used:

```bash
# Typically tcsh is used on "rcas" nodes so this example is for tcsh
# First, add custom SDCC location for Python 3 to PATH
setenv PATH /u0b/software/jupyter/python/3.8.0/bin:$PATH
cd
mkdir .virtualenvs # the exact name is unimportant
python3 -m venv .virtualenvs/reana
source .virtualenvs/reana/bin/activate.csh
pip install reana-client
rehash
```

After the installation process is finished it is a good idea to check if
the client is functional, for example
```bash
# Check if it's alive
reana-client --help
```

The "activate" step will be necessary every time a new shell/window is created
for interacting with REANA. If no longer necessary, the virtual environment can
be deactivated. A full session will look something like:

```bash
# Enter the virtual environment
source ~/.virtualenvs/reana/bin/activate
# ... REANA commands here...
# Leave the virtual environment
deactivate
```
A SSH tunnel is required to access the REANA cluster at BNL from an outside location.
```bash
# Establish a SSH tunnel
ssh -L 30443:kubmaster01.sdcc.bnl.gov:30443 ssh.sdcc.bnl.gov
```

Assuming a token has been obtained and a SSH tunnel established on port 30443
a test session might look like this:
```bash
# Assuming the user is running bash:
# Set REANA environment variables for the client
export REANA_SERVER_URL=https://localhost:30443
export REANA_ACCESS_TOKEN=________ # user's REANA token
# clone and run a simple analysis example
git clone https://github.com/reanahub/reana-demo-root6-roofit
cd reana-demo-root6-roofit
reana-client run -w root6-roofit
```

Alternatively, when working within the BNL perimeter i.e. on the interactive nodes
the server needs to be specified directly i.e. without the ssh redirection:
```bash
export REANA_SERVER_URL=https://kubmaster01.sdcc.bnl.gov:30443
```

The above example will need to be adjusted for tcsh if necessary.

##### Workflow definition and custom name
By default the client will look up the workflow definition from the file ```reana.yaml```
found in the current folder.
The ```-w``` option ("workflow") simply defines the handle/name by which this workflow will
be know to the system. The name can be anything. To specify a different workflow definition
file and a different name one might use something like
```bash
reana-client run -f my_workflow_file.yaml -w my_custom_workflow_name
```
Progress of REANA workflows can be tracked in the Web-based GUI provided by each cluster
or via the CLI, *reana-client*. Likewise, outputs files generated by the workflows
(including the example above) are available for download both via the GUI and the CLI.
If a workflow is no longer useful it can be deleted from the REANA system:
```bash
reana-client delete -w my_custom_workflow_name
```
##### Useful Options
List of (many) commands that can be used with the client can be easily referenced by
using its ```--help``` option. There are also other options, some of the more
useful ones are listed here (mostly overriding default values):
```bash
-w name of the workflow
-t access token
-f file (default is "reana.yaml")
-o path to the directory where the files are to be downloaded
```

##### Caveats
One of the available options in the definition of a REANA workflow is ```directories```.
This option is not mandatory and performs a helper function in cases when contents of
a whole directory should be staged to the workspace of a running REANA process. This
can have unintended consequences, for example an attempt to stage a massive AFS
folder or some other file system with inherent latency or of a large size may result
in a lot of network traffic on the submitting host and the whole process taking
an unreasonably long time. Issues with storage quotas on the REANA cluster are also
possible.
**Caution must be exercised**.
