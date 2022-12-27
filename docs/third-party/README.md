# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://github.com/sthagen/pilli/blob/default/sbom.json) with SHA256 checksum ([4caaaafe ...](https://raw.githubusercontent.com/sthagen/pilli/default/sbom.json.sha256 "sha256:4caaaafe0714758c6b41dd3a03debc520f25d3d8941055feb2bee68b838d2abd")).
<!--[[[end]]] (checksum: 0a116e61e28ea09f926b7f81193b6977)-->
## Licenses

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                             | Version                                             | License     | Author                      | Description (from packaging data)                                       |
|:-------------------------------------------------|:----------------------------------------------------|:------------|:----------------------------|:------------------------------------------------------------------------|
| [openpyxl](https://openpyxl.readthedocs.io)      | [3.0.10](https://pypi.org/project/openpyxl/3.0.10/) | MIT License | See AUTHORS                 | A Python library to read/write Excel 2010 xlsx/xlsm files               |
| [pandas](https://pandas.pydata.org)              | [1.5.2](https://pypi.org/project/pandas/1.5.2/)     | BSD License | The Pandas Development Team | Powerful data structures for data analysis, time series, and statistics |
| [pydantic](https://github.com/pydantic/pydantic) | [1.10.2](https://pypi.org/project/pydantic/1.10.2/) | MIT License | Samuel Colvin               | Data validation and settings management using python type hints         |
| [typer](https://github.com/tiangolo/typer)       | [0.7.0](https://pypi.org/project/typer/0.7.0/)      | MIT License | Sebastián Ramírez           | Typer, build great CLIs. Easy to code. Based on Python type hints.      |
<!--[[[end]]] (checksum: a9410384a157aa2b6e668ce6c64d187d)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                        | Version                                                  | License                              | Author                    | Description (from packaging data)                          |
|:------------------------------------------------------------|:---------------------------------------------------------|:-------------------------------------|:--------------------------|:-----------------------------------------------------------|
| [click](https://palletsprojects.com/p/click/)               | [8.1.3](https://pypi.org/project/click/8.1.3/)           | BSD License                          | Armin Ronacher            | Composable command line interface toolkit                  |
| [et-xmlfile](https://foss.heptapod.net/openpyxl/et_xmlfile) | [1.1.0](https://pypi.org/project/et-xmlfile/1.1.0/)      | MIT License                          | See ATUHORS.txt           | An implementation of lxml.xmlfile for the standard library |
| [numpy](https://www.numpy.org)                              | [1.24.0](https://pypi.org/project/numpy/1.24.0/)         | BSD License                          | Travis E. Oliphant et al. | Fundamental package for array computing in Python          |
| [python-dateutil](https://github.com/dateutil/dateutil)     | [2.8.2](https://pypi.org/project/python-dateutil/2.8.2/) | Apache Software License; BSD License | Gustavo Niemeyer          | Extensions to the standard Python datetime module          |
| [pytz](http://pythonhosted.org/pytz)                        | [2022.7](https://pypi.org/project/pytz/2022.7/)          | MIT License                          | Stuart Bishop             | World timezone definitions, modern and historical          |
| [six](https://github.com/benjaminp/six)                     | [1.16.0](https://pypi.org/project/six/1.16.0/)           | MIT License                          | Benjamin Peterson         | Python 2 and 3 compatibility utilities                     |
<!--[[[end]]] (checksum: 6e2a6462503c3fa20a6b4ac76b0389de)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
openpyxl==3.0.10
  - et-xmlfile [required: Any, installed: 1.1.0]
pandas==1.5.2
  - numpy [required: >=1.21.0, installed: 1.24.0]
  - python-dateutil [required: >=2.8.1, installed: 2.8.2]
    - six [required: >=1.5, installed: 1.16.0]
  - pytz [required: >=2020.1, installed: 2022.7]
pydantic==1.10.2
  - typing-extensions [required: >=4.1.0, installed: 4.4.0]
typer==0.7.0
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
````
<!--[[[end]]] (checksum: e1db8ad8dcdb167c8154790c62b9b630)-->
