from setuptools import setup, find_packages
setup(
    name = 'pipeline_0101',
    version = '1.0',
    packages = find_packages(include = ('pipeline_0101*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.6.7'],
    entry_points = {
'console_scripts' : [
'main = pipeline_0101.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
