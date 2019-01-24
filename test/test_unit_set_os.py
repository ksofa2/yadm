"""Unit tests: set_operating_system"""
import pytest


@pytest.mark.parametrize(
    'proc_value, expected_os', [
        ('missing', 'uname'),
        ('has Microsoft inside', 'WSL'),
        ('another value', 'uname'),
    ], ids=[
        '/proc/version missing',
        '/proc/version includes MS',
        '/proc/version excludes MS',
    ])
def test_set_operating_system(
        runner, paths, tst_sys, proc_value, expected_os):
    """Run ,set_operating_system and test result"""
    proc_version = paths.root.join('proc_version')
    if proc_value != 'missing':
        proc_version.write(proc_value)
    script = f"""
        YADM_TEST=1 source {paths.pgm}
        PROC_VERSION={proc_version}
        set_operating_system
        echo $OPERATING_SYSTEM
    """
    run = runner(command=['bash'], inp=script)
    print(script)
    run.report()
    if expected_os == 'uname':
        expected_os = tst_sys
    assert run.out.rstrip() == expected_os
