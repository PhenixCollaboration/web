---
name: cwl
layout: newbase
---

<h3>Common Workflow Language</h3>

* TOC
{:toc}

##### Overview
The Common Workflow Langeuate (or
{% include navigation/findlink.md name='cwl' tag='CWL' %})
is a popular format in which to describe complex workflows.
It is used in
{% include navigation/findlink.md name='reana' tag='REANA' %}
in cases where the serial workflow decriptions (which are
very simple to use ) are insufficient. A typical example of
CWL use in REANA is to describe parallel components of the
workflow, in cases where parallel execution is optimal.

The semantics of CWL is fairly deep and its use involves
a learning curve. It is uses with a number of platforms
including
{% include navigation/findlink.md name='reana' tag='REANA' %}
and
[Apache Airflow](https://airflow.apache.org/){:target="_blank"}.
A detailed
{% include navigation/findlink.md name='cwl_user_guide' tag='CWL User Guide' %}
is available.

##### Parallel Wokrflows

Parallel worflows are termed as "scattered" in CWL terminology.
An example of syntax used in such cases is available on the
["scatter workflow" page](https://www.commonwl.org/user_guide/23-scatter-workflow/index.html){:target="_blank"}
in the 
{% include navigation/findlink.md name='cwl_user_guide' tag='CWL User Guide' %}.

The YAML description of a scattered workflow must include the directive
```yaml
requirements:
  ScatterFeatureRequirement: {}
```