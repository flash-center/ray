"""By importing this module, common derivied fields are registered with yt."""

from yt.data_objects.field_info_container import add_field

def _nele(field, data):
    return data['ye'] * data['dens'] * data['sumy'] * 6.022E23

add_field('nele', function=_nele, take_log=True)


def _abar(field, data):
    return 1.0 / data['sumy']

add_field('abar', function=_abar, take_log=False)
