from antlr4 import InputStream, CommonTokenStream

from antlr.JavaLexer import JavaLexer
from antlr.JavaParser import JavaParser
from antlr.JavaParserListener import JavaParserListener

class FileGrammer:

    def executeFile(self,extension,code):
        switch = {
            "java": self.getJavaGrammar
        }
        return switch.get(extension, lambda: "No options found")(code)

    def getJavaGrammar(self,code):
        codeStream = InputStream(code)
        lexer = JavaLexer(codeStream)
        tokensStream = CommonTokenStream(lexer)
        parser = JavaParser(tokensStream)
        tree = parser.compilationUnit()
        return {'tree':tree,'parser':parser,'lexer':lexer}
