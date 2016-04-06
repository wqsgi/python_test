import re

__author__ = 'weiqisong'


class CodeBuilder:
    INDENT_STEP = 4

    def __init__(self):
        self._lines = []
        self._level = 0

    def add_line(self, line):
        self._lines.extend([self._level * " ", line, "\n"])

    def __str__(self):
        return "".join(str(line) for line in self._lines)

    def indent(self):
        self._level += self.INDENT_STEP * 1

    def dedent(self):
        self._level -= self.INDENT_STEP * 1

    def add_section(self):
        section = CodeBuilder()
        self._lines.append(section)
        return section

    def get_global(self):
        context = []
        code = str(self)
        exec(code, context)
        return context


class template:
    def __init__(self, text, *contents):
        self.context = []
        self._text = text
        self.code = CodeBuilder()

        self.var_all = []

        vars_code = self.create_function()
        tokens = re.split(r"(?s)({{.*?}}|{%.*?%}|{#.*?#})", text)
        for token in tokens:
            if token.startswith("{#"):
                continue

            elif token.startswith("{{"):
                expr = self._expr_code(token[2,-2])



    def _expr_code(self, expr):
        if "|" in expr:
            pipes = expr.split("|")
            code = self._expr_code(pipes[0])
            for func in pipes[1:]:
                self._variable(func, self.all_vars)
                code = "c_%s(%s)" % (func, code)
        elif "." in expr:
            dots = expr.split(".")
            code = self._expr_code(dots[0])
            args = ", ".join(repr(d) for d in dots[1:])
            code = "do_dots(%s, %s)" % (code, args)
        else:
            self._variable(expr, self.all_vars)
            code = "c_%s" % expr
        return code

    def _variable(self, name, vars_set):
        """Track that `name` is used as a variable.

        Adds the name to `vars_set`, a set of variable names.

        Raises an syntax error if `name` is not a valid name.

        """
        if not re.match(r"[_a-zA-Z][_a-zA-Z0-9]*$", name):
            self._syntax_error("Not a valid name", name)
        vars_set.add(name)

    def create_function(self):
        self.code.add_line("def render_function(context, do_dots):")
        self.code.indent()
        vars_code = self.code.add_section()
        self.code.add_line("result = []")
        self.code.add_line("append_result = result.append")
        self.code.add_line("extend_result = result.extend")
        self.code.add_line("to_str = str")
        return vars_code

        # def parse(self):
