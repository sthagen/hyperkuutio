"""Hypercube (Finnish: hyperkuutio) tool that scratches some itch."""

# [[[fill git_describe()]]]
__version__ = '2023.10.29+parent.eb232c96'
# [[[end]]] (checksum: 36c4e1051de6e12ead959b1b636cbfc2)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
