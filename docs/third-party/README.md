# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/hyperkuutio/blob/default/etc/sbom/cdx.json) with SHA256 checksum ([f31889b0 ...](https://git.sr.ht/~sthagen/hyperkuutio/blob/default/etc/sbom/cdx.json.sha256 "sha256:f31889b09bdcac1dffc77ea503e46aac1e368cd46c8a9495bb886b9dde4761f6")).
<!--[[[end]]] (checksum: 0bc65db75253e50077245993f4f0ee3f)-->
## Licenses

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                             | Version                                           | License     | Author                                                                                                                                                                                                                                                                                                                                                                                                                           | Description (from packaging data)                                       |
|:-------------------------------------------------|:--------------------------------------------------|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------|
| [openpyxl](https://openpyxl.readthedocs.io)      | [3.1.2](https://pypi.org/project/openpyxl/3.1.2/) | MIT License | See AUTHORS                                                                                                                                                                                                                                                                                                                                                                                                                      | A Python library to read/write Excel 2010 xlsx/xlsm files               |
| [pandas](https://pandas.pydata.org)              | [2.1.3](https://pypi.org/project/pandas/2.1.3/)   | BSD License | The Pandas Development Team <pandas-dev@python.org>                                                                                                                                                                                                                                                                                                                                                                              | Powerful data structures for data analysis, time series, and statistics |
| [pydantic](https://github.com/pydantic/pydantic) | [2.5.2](https://pypi.org/project/pydantic/2.5.2/) | MIT License | Samuel Colvin <s@muelcolvin.com>, Eric Jolibois <em.jolibois@gmail.com>, Hasan Ramezani <hasan.r67@gmail.com>, Adrian Garcia Badaracco <1755071+adriangb@users.noreply.github.com>, Terrence Dorsey <terry@pydantic.dev>, David Montague <david@pydantic.dev>, Serge Matveenko <lig@countzero.co>, Marcelo Trylesinski <marcelotryle@gmail.com>, Sydney Runkle <sydneymarierunkle@gmail.com>, David Hewitt <mail@davidhewitt.io> | Data validation using Python type hints                                 |
| [typer](https://github.com/tiangolo/typer)       | [0.9.0](https://pypi.org/project/typer/0.9.0/)    | MIT License | Sebastián Ramírez                                                                                                                                                                                                                                                                                                                                                                                                                | Typer, build great CLIs. Easy to code. Based on Python type hints.      |
<!--[[[end]]] (checksum: 2030423d02da31192c430375c9a9c508)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                             | Version                                                    | License                              | Author                                                                                | Description (from packaging data)                          |
|:-----------------------------------------------------------------|:-----------------------------------------------------------|:-------------------------------------|:--------------------------------------------------------------------------------------|:-----------------------------------------------------------|
| [click](https://palletsprojects.com/p/click/)                    | [8.1.5](https://pypi.org/project/click/8.1.5/)             | BSD License                          | Pallets <contact@palletsprojects.com>                                                 | Composable command line interface toolkit                  |
| [et-xmlfile](https://foss.heptapod.net/openpyxl/et_xmlfile)      | [1.1.0](https://pypi.org/project/et-xmlfile/1.1.0/)        | MIT License                          | See ATUHORS.txt                                                                       | An implementation of lxml.xmlfile for the standard library |
| [numpy](https://www.numpy.org)                                   | [1.25.1](https://pypi.org/project/numpy/1.25.1/)           | BSD License                          | Travis E. Oliphant et al.                                                             | Fundamental package for array computing in Python          |
| [python-dateutil](https://github.com/dateutil/dateutil)          | [2.8.2](https://pypi.org/project/python-dateutil/2.8.2/)   | Apache Software License; BSD License | Gustavo Niemeyer                                                                      | Extensions to the standard Python datetime module          |
| [pytz](http://pythonhosted.org/pytz)                             | [2023.3](https://pypi.org/project/pytz/2023.3/)            | MIT License                          | Stuart Bishop                                                                         | World timezone definitions, modern and historical          |
| [six](https://github.com/benjaminp/six)                          | [1.16.0](https://pypi.org/project/six/1.16.0/)             | MIT License                          | Benjamin Peterson                                                                     | Python 2 and 3 compatibility utilities                     |
| [typing_extensions](https://github.com/python/typing_extensions) | [4.7.1](https://pypi.org/project/typing_extensions/4.7.1/) | Python Software Foundation License   | "Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee" <levkivskyi@gmail.com> | Backported and Experimental Type Hints for Python 3.7+     |
<!--[[[end]]] (checksum: a5e00ef11689863f3ca4ba0475a3f260)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
openpyxl==3.1.2
└── et-xmlfile [required: Any, installed: 1.1.0]
pandas==2.1.3
├── numpy [required: >=1.22.4,<2, installed: 1.25.1]
├── python-dateutil [required: >=2.8.2, installed: 2.8.2]
│   └── six [required: >=1.5, installed: 1.16.0]
├── pytz [required: >=2020.1, installed: 2023.3]
└── tzdata [required: >=2022.1, installed: 2023.3]
pydantic==2.5.2
├── annotated-types [required: >=0.4.0, installed: 0.5.0]
├── pydantic-core [required: ==2.14.5, installed: 2.14.5]
│   └── typing-extensions [required: >=4.6.0,!=4.7.0, installed: 4.7.1]
└── typing-extensions [required: >=4.6.1, installed: 4.7.1]
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.5]
└── typing-extensions [required: >=3.7.4.3, installed: 4.7.1]
````
<!--[[[end]]] (checksum: aedbb8df807efd58030e4e9f8ff9bfcd)-->
