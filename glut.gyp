#
# glut.gyp
#
{
  'targets' : [
    {
      'target_name': 'glut_static',
      'type': 'static_library',
      'include_dirs': [
        'glut-3.7/include',
      ],
      'sources': [
        'glut-3.7/lib/glut/glut.def',
        'glut-3.7/lib/glut/glut_8x13.c',
        'glut-3.7/lib/glut/glut_9x15.c',
        'glut-3.7/lib/glut/glut_bitmap.c',
        'glut-3.7/lib/glut/glut_bwidth.c',
        'glut-3.7/lib/glut/glut_cindex.c',
        'glut-3.7/lib/glut/glut_cmap.c',
        'glut-3.7/lib/glut/glut_cursor.c',
        'glut-3.7/lib/glut/glut_dials.c',
        'glut-3.7/lib/glut/glut_dstr.c',
        'glut-3.7/lib/glut/glut_event.c',
        'glut-3.7/lib/glut/glut_ext.c',
        'glut-3.7/lib/glut/glut_fullscrn.c',
        'glut-3.7/lib/glut/glut_gamemode.c',
        'glut-3.7/lib/glut/glut_get.c',
        'glut-3.7/lib/glut/glut_glxext.c',
        'glut-3.7/lib/glut/glut_hel10.c',
        'glut-3.7/lib/glut/glut_hel12.c',
        'glut-3.7/lib/glut/glut_hel18.c',
        'glut-3.7/lib/glut/glut_init.c',
        'glut-3.7/lib/glut/glut_input.c',
        'glut-3.7/lib/glut/glut_joy.c',
        'glut-3.7/lib/glut/glut_key.c',
        'glut-3.7/lib/glut/glut_keyctrl.c',
        'glut-3.7/lib/glut/glut_keyup.c',
        'glut-3.7/lib/glut/glut_menu.c',
        'glut-3.7/lib/glut/glut_mesa.c',
        'glut-3.7/lib/glut/glut_modifier.c',
        'glut-3.7/lib/glut/glut_mroman.c',
        'glut-3.7/lib/glut/glut_overlay.c',
        'glut-3.7/lib/glut/glut_roman.c',
        'glut-3.7/lib/glut/glut_shapes.c',
        'glut-3.7/lib/glut/glut_space.c',
        'glut-3.7/lib/glut/glut_stroke.c',
        'glut-3.7/lib/glut/glut_swap.c',
        'glut-3.7/lib/glut/glut_swidth.c',
        'glut-3.7/lib/glut/glut_tablet.c',
        'glut-3.7/lib/glut/glut_teapot.c',
        'glut-3.7/lib/glut/glut_tr10.c',
        'glut-3.7/lib/glut/glut_tr24.c',
        'glut-3.7/lib/glut/glut_util.c',
        'glut-3.7/lib/glut/glut_vidresize.c',
        'glut-3.7/lib/glut/glut_warp.c',
        'glut-3.7/lib/glut/glut_win.c',
        'glut-3.7/lib/glut/glut_winmisc.c',
        'glut-3.7/lib/glut/win32_glx.c',
        'glut-3.7/lib/glut/win32_menu.c',
        'glut-3.7/lib/glut/win32_util.c',
        'glut-3.7/lib/glut/win32_winproc.c',
        'glut-3.7/lib/glut/win32_x11.c',
      ],
      'conditions': [
        ['OS=="win"', {
          'product_name': 'glut32',
          'sources!' : [
            'glut-3.7/lib/glut/glut_glxext.c',
            'glut-3.7/lib/glut/glut_menu.c',
          ],
        }], # OS="win"
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'glut-3.7/include/',
        ],
      },
    }, # target: glut_static
    {
      'target_name': 'glut_shared',
      'type': 'shared_library',
      'dependencies': [
        'glut_static',
      ],
      'export_dependent_settings': [
        'glut_static',
      ],
      'conditions': [
        ['OS=="win"', {
          'product_name': 'glut32',
          'sources': [
            'glut-3.7/lib/glut/glut.def',
          ],
        }], # OS="win"
      ],
    }, # target: glut_shared
  ],
}
# vim:sts=2:sw=2:norl
