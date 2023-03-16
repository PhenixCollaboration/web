---
name: reana
layout: newbase
---

<h3>REANA</h3>

* TOC
{:toc}

##### Overview
{% include navigation/findlink.md name='reana' tag='REANA' %}
is a reproducible research data analysis platform developed at CERN.
It is used for Analysis Preservation in PHENIX due to the following features:

* Unambiguous description of workflows (encoded in YAML)
* Capture and preservation of both the software and the software environment by using **containerization**

REANA workflows can be represented as *Directed Acyclic Graphs* which is reflected in
the YAML schema based on the 
{% include navigation/findlink.md name='cwl' tag='Common Workflow Language (CWL)' %}
as one of the options. Simpler options are available. For example,
current PHENIX analyses do not rely on CWL and are preserved as combinations of _linear_ workflows
to reduce complexity. This approach does not require specialized syntax and
logic (as in the Common Workflow Language) and the worrflows are formatted
as simple YAML list structures.

##### REANA Cluster
Execution of workflows in REANA takes place on machines configured as a **REANA cluster**.
CERN was the first site to deploy such cluster, however currently these
installations are available at a number of institutions including BNL.
It is available on the internal BNL network, with outside access possible using
either SSH tunneling or VPN.

> The cluster is separate from the rest of the computing facility in the sense
> that it does not share any file systems with the rest of the machines at BNL.
> Interaction with the REANA cluster is only possible using its network
> interface (HTTPS). A Web GUI if available for quick monitoring of the user's
> workflows in various stages of execution.
>
> Full access to all REANA functions is possible with the CLI client. Importantly,
> the client is used to stage in the input data, configuration and other necessary
> data products if necessary. The client is also used to stage out the outputs
> of the completed workflows i.e. bring these data to a desired location. As
> stated above, REANA machines do not have direct access to shared file systems
> like interactive or batch worker nodes at BNL. The software client must be used
> for bringing data to and from the REANA machines.

##### The Token
*Access to the REANA cluster at BNL is controlled by the administrators. If approved,
the user will be able to obtain an access token which will then be used by the client
software (as a properly set environment variable) to authenticate to the cluster*.

To initiate this process the user must first apply for an account
by choosing the "sign up" option in the Web interface. In case of BNL having a valid SDCC
account is a prerequisite for approval. Once an account is created, it becomes possible
to log in and then the user can obtain their REANA *access token* in the profile section
in the upper right corner of the REANA web page.

##### REANA Client
###### Client installation using Python virtual environment
Client software must be installed on the user's machine.
It is Python-based and at the time of writing Python 3.6 and higher is recommended.
Perhaps the most efficient way to do the installation is via the Python "virtual environment"
mechanism, as illustrated below. Compatibility among the many components which are
part of this installation is not a trivial issue, so after some testing
the following Python version and instance is recommended at the SDCC:
```bash
/direct/u0b/software/jupyter/python/3.8.0/bin/python3.8
```

In the following, references to `python3` should be expanded to the above.
Setting up virtual environment:

```bash
# Let's use bash in this example
cd
mkdir .virtualenvs # the exact name is unimportant
python3 -m venv .virtualenvs/reana
source .virtualenvs/reana/bin/activate
pip install reana-client
rehash
```

It is a good idea to instal the `wheel` package before installing `reana-client`
since it will make the installation faster. This is done, as expected, as follows:
```bash
pip install wheel
```

Depending on the system, additional softare may need to be installed
for this installation procss to work, for example `gcc` compiler. On Debian-based
Linux distros, this can be accomplished by
```bash
sudo apt install build-essential
# make sure the link expected by the wheel package does exist:
ls -l /usr/bin/x86_64-linux-gnu-gcc
# at the time of writing, it often points to gcc-10
```


At the time of writing, the server instance running at BNL, used for PHENIX work,
is at version 0.7.1, so to ensure compatibility you will likely need to force same
version for the installed client:
```
pip3 install --upgrade reana-client==0.7.1
```

The "activate" step included in the example above is necessary every time a new
shell/window is created for interacting with REANA. If no longer necessary, the
virtual environment can be deactivated. A full session will look something like:


```bash
# Using bash here
# Entering the virtual environment
#
source ~/.virtualenvs/reana/bin/activate
# ... REANA commands here...
# ... Do something useful...
# Leave the virtual environment
deactivate
```

###### Getting help with/from the client

After the installation process is finished it is a good idea to check if
the client is functional, for example
```bash
# Check if it's alive - should print a help screen
reana-client --help
```
The client is equipped with very helpful nested help screens i.e. each command
will also accept the "--help" option which will cause it to print help
information specific for that command. For example:
```bash
reana-client download --help
# ...will output help information specific to the "download" command
```
###### Connecting to the service from a outside location
A SSH tunnel is required to access the REANA cluster at BNL from an outside location.
```bash
# Establish a SSH tunnel
ssh -L 30443:kubmaster01.sdcc.bnl.gov:30443 ssh.sdcc.bnl.gov
```

Assuming a token has been obtained and a SSH tunnel established on port 30443
a test session might look like this:
```bash
# Using bash
# Set REANA environment variables for the client
export REANA_SERVER_URL=https://localhost:30443
export REANA_ACCESS_TOKEN=________ # user's REANA token
reana-client ping
```

You should see the versions of the client and the server printed out,
and a message indicating a successful connection. If this works, you can
proceed to a demo:

```bash
#
# Clone and run a standard simple analysis example
git clone https://github.com/reanahub/reana-demo-root6-roofit
cd reana-demo-root6-roofit
reana-client run -w root6-roofit
```

The status of the workflow can now be checked using either the client, or the REANA Web UI.
In the latter case, assuming the user is doing that on their workstation outside of the BNL
perimeter (e.g. at home), and established a SSH tunnel
as explained above, this is done by pointing the browser to `https://localhost:30443`.
On the internal BNL network the correct URL will be `https://kubmaster01.sdcc.bnl.gov:30443`.

###### Connecting to the service from BNL (SDCC)

Working with REANA using interactive nodes of the SDCC cluster may be preferable
when substantial amounts of data need to be staged in or out of REANA, especially
if these data is more accessible at the SDCC facility. Remember that every
REANA workflow needs to stage data, and if you are using your laptop (e.g. at home)
that machine needs to have that data somehow available. So things may be
easier in the cases if run at SDCC.

When working within the BNL perimeter i.e. on the interactive nodes
such as "rcas" machines the procedure of using the client is exactly the same
however the server URL for the client needs to be specified directly as opposed to
the ssh tunnel:
```bash
# If running bash:
export REANA_SERVER_URL=https://kubmaster01.sdcc.bnl.gov:30443
#
#
# If running tcsh:
setenv REANA_SERVER_URL https://kubmaster01.sdcc.bnl.gov:30443
#
```

Once again, it's a good idea to validate the connection to the server:

```bash
reana-client ping
```

This command should complete without errors.


###### Connecting to the new instance of the REANA cluster

As of late 2022, there is a new instance of REANA being tested at BNL.
While fully accessible within the BNL perimeter, the normal SSH tunnel
won't work for users wishing to access this service from an external
location. In this case, a `SOCKS` proxy will need to be set up. First,
connect to a SDCC machine to use it as a proxy:

```bash
# specify the correct username
ssh -D localhost:8031 -J user@ssh.sdcc.bnl.gov user@rcas2071.rcf.bnl.gov
```

Then, start the browser of your choice with the option to use this proxy.
For example, with Chrome the following command can be used

```bash
# Use the URL: https://reana.apps.usatlas.bnl.gov/
google-chrome-stable --proxy-server="socks5://localhost:8031"
```

##### Custom Workflow Definition File and Custom Workflow Name

REANA uses the following defaults when operating the ```reana-client```:
* The client will look up the workflow definition from the file ```reana.yaml```
found in the current folder.
* The workflow, when activated in the system, will be named simply "workflow"

This defauls behaviors can be changed if needed by using options:
* ```-f``` will inform the client that the workflow definition needs to be read
from the user-specified file, not from the default ```reana.yaml```
* ```-w``` allows the user to assign custom names to workflows.

Example:
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
-o path to the directory where the files are to be downloaded # for the "download" command
```

##### Tutorials
* For basic tutorials please see
{% include navigation/findlink.md name='reana_tutorials' tag='the relevant section of the PHENIX GitHub repository' -%}.
* For a demonstration of a real case of final analysis done reana please see
{% include navigation/findlink.md name='reana_pi0' tag='pi0/gamma demo' %} on GitHub.

##### Caveats
###### Directories
One of the available options in the definition of a REANA workflow is ```directories```.
This option is not mandatory and performs a helper function in cases when contents of
a whole directory should be staged to the workspace of a running REANA process. This
can have unintended consequences, for example an attempt to stage a massive AFS
folder or some other file system with inherent latency or of a large size may result
in a lot of network traffic on the submitting host and the whole process taking
an unreasonably long time. Issues with storage quotas on the REANA cluster are also
possible.
**Caution must be exercised**.

###### Cleanup
If the user decides to delete a workflow, the respective workspace (i.e. the sandbox
storage where jobs were wun) won't be deleted by default, which may cause confusion.
To perform the deletion of both the workflow and data associated with it, one
must use correponding command line options, for example:
```bash
reana-client delete --include-workspace -w my_workflow.1
```
To remove a workflow from the system completely, including any traces in the Web interface,
the "--include-records" option should be added.
