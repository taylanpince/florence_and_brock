from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from django_extensions.management.modelviz import generate_dot

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--disable-fields', '-d', action='store_true', dest='disable_fields',
            help='Do not show the class member fields'),
        make_option('--group-models', '-g', action='store_true', dest='group_models',
            help='Group models together respective to there application'),
        make_option('--all-applications', '-a', action='store_true', dest='all_applications',
            help='Automaticly include all applications from INSTALLED_APPS'),
        make_option('--output', '-o', action='store', dest='outputfile',
            help='Render output file. Type of output dependend on file extensions. Use png or jpg to render graph to image.'),
        make_option('--layout', '-l', action='store', dest='layout', default='dot',
            help='Layout to be used by GraphViz for visualization. Layouts: circo dot fdp neato nop nop1 nop2 twopi'),
    )

    help = ("Creates a GraphViz dot file for the specified app names.  You can pass multiple app names and they will all be combined into a single model.  Output is usually directed to a dot file.")
    args = "[appname]"
    label = 'application name'

    requires_model_validation = True
    can_import_settings = True

    def handle(self, *args, **options):
        if len(args) < 1 and not options['all_applications']:
            raise CommandError("need one or more arguments for appname")

        dotdata = generate_dot(args, **options)
        if options['outputfile']:
            self.render_output(dotdata, **options)
        else:
            self.print_output(dotdata)

    def print_output(self, dotdata):
        print dotdata

    def render_output(self, dotdata, **kwargs):
        try:
            import pygraphviz
        except ImportError, e:
            raise CommandError("need pygraphviz python module ( apt-get install python-pygraphviz )")

        vizdata = ' '.join(dotdata.split("\n")).strip()
        if [int(v) for v in pygraphviz.__version__.split('.')]<(0,36):
            ##raise CommandError("need version 0.36 or higher of pygraphviz")
            # HACK around old/broken AGraph before version 0.36 (ubuntu ships with this old version)
            import tempfile
            tmpfile = tempfile.NamedTemporaryFile()
            tmpfile.write(vizdata)
            tmpfile.seek(0)
            vizdata = tmpfile.name
        graph = pygraphviz.AGraph(vizdata)
        graph.layout(prog=kwargs['layout'])
        graph.draw(kwargs['outputfile'])

