# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TrenchDrawer
                                 A QGIS plugin
 Plugin for drawing trenches
                             -------------------
        begin                : 2016-05-10
        copyright            : (C) 2016 by L - P : Archaeology
        email                : m.johnson@lparchaeology.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load TrenchDrawer class from file TrenchDrawer.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .trench_drawer import TrenchDrawer
    return TrenchDrawer(iface)
