#
# glut.gyp
#
{
  'targets' : [
    {
      'target_name': 'glut_lib',
      'type': 'static_library',
      'include_dirs': [
        '../src/include',
      ],
      'sources': [
        '../src/lib/glut/glut.def',
        '../src/lib/glut/glut_8x13.c',
        '../src/lib/glut/glut_9x15.c',
        '../src/lib/glut/glut_bitmap.c',
        '../src/lib/glut/glut_bwidth.c',
        '../src/lib/glut/glut_cindex.c',
        '../src/lib/glut/glut_cmap.c',
        '../src/lib/glut/glut_cursor.c',
        '../src/lib/glut/glut_dials.c',
        '../src/lib/glut/glut_dstr.c',
        '../src/lib/glut/glut_event.c',
        '../src/lib/glut/glut_ext.c',
        '../src/lib/glut/glut_fullscrn.c',
        '../src/lib/glut/glut_gamemode.c',
        '../src/lib/glut/glut_get.c',
        '../src/lib/glut/glut_glxext.c',
        '../src/lib/glut/glut_hel10.c',
        '../src/lib/glut/glut_hel12.c',
        '../src/lib/glut/glut_hel18.c',
        '../src/lib/glut/glut_init.c',
        '../src/lib/glut/glut_input.c',
        '../src/lib/glut/glut_joy.c',
        '../src/lib/glut/glut_key.c',
        '../src/lib/glut/glut_keyctrl.c',
        '../src/lib/glut/glut_keyup.c',
        '../src/lib/glut/glut_menu.c',
        '../src/lib/glut/glut_mesa.c',
        '../src/lib/glut/glut_modifier.c',
        '../src/lib/glut/glut_mroman.c',
        '../src/lib/glut/glut_overlay.c',
        '../src/lib/glut/glut_roman.c',
        '../src/lib/glut/glut_shapes.c',
        '../src/lib/glut/glut_space.c',
        '../src/lib/glut/glut_stroke.c',
        '../src/lib/glut/glut_swap.c',
        '../src/lib/glut/glut_swidth.c',
        '../src/lib/glut/glut_tablet.c',
        '../src/lib/glut/glut_teapot.c',
        '../src/lib/glut/glut_tr10.c',
        '../src/lib/glut/glut_tr24.c',
        '../src/lib/glut/glut_util.c',
        '../src/lib/glut/glut_vidresize.c',
        '../src/lib/glut/glut_warp.c',
        '../src/lib/glut/glut_win.c',
        '../src/lib/glut/glut_winmisc.c',
        '../src/lib/glut/win32_glx.c',
        '../src/lib/glut/win32_menu.c',
        '../src/lib/glut/win32_util.c',
        '../src/lib/glut/win32_winproc.c',
        '../src/lib/glut/win32_x11.c',
      ],
      'conditions': [
        ['OS=="win"', {
          'product_name': 'glut32',
          'sources!' : [
            '../src/lib/glut/glut_glxext.c',
            '../src/lib/glut/glut_menu.c',
          ],
        }], # OS="win"
      ],
    }, # target: glut_lib
    {
      'target_name': 'glut_dll',
      'type': 'shared_library',
      'dependencies': [
        'glut_lib',
      ],
      'conditions': [
        ['OS=="win"', {
          'product_name': 'glut32',
          'sources': [
            '../src/lib/glut/glut.def',
          ],
        }], # OS="win"
      ],
    }, # target: glut_dll
  ],
}
# vim:sts=2:sw=2:norl
