import string

import pytest

from vkwave.vkscript import execute

TEST_STRING = string.printable


@execute
def demo_build():
    pass


def test_build():
    code = demo_build.build()
    assert code == ""


@execute
def demo_assignments():
    test = 0
    test = TEST_STRING
    test = ()
    test = []
    test = {}
    test = True
    test = False
    test = None
    tmp = [0, TEST_STRING, (), [], {}]
    test = tmp
    del test, tmp

    # Augmented Assignments
    test = 0
    test += 1
    test -= 1
    test /= 1
    test *= 1
    test >>= 1
    test <<= 1
    test **= 1
    test |= 1
    test &= 1
    test %= 1
    del test


@execute
def demo_functions():
    test = [0, 1, 3, 4]
    tmp = test[0:2]  # noqa
    end = test.pop()
    begin = test.shift()
    test.unshift(begin)
    test.append(end)
    test.splice(1, 2, 3, 3)
    test = "aba"
    test.split("b")
    test.substr(1, 2)


@execute
def demo_blocks():
    test = []
    i = 1
    while i <= 10:
        test.append(i)
        i += 1

    if len(test) == 10:
        return "ok"
    elif i == 1:
        return "oops..."
    else:
        return "oops..."


def test_converter():
    assignments = demo_assignments.build()
    functions = demo_functions.build()
    blocks = demo_blocks.build()
    assert assignments == (
        "var test=0;"
        f"var test={repr(TEST_STRING)};"
        "var test=[];"
        "var test=[];"
        "var test={};"
        "var test=true;"
        "var test=false;"
        "var test=null;"
        f"var tmp=[0,{repr(TEST_STRING)},[],[],{{}}];"
        "var test=tmp;"
        "delete test;"
        "delete tmp;"
        "var test=0;"
        "test=test+(1);"
        "test=test-(1);"
        "test=test/(1);"
        "test=test*(1);"
        "test=test>>(1);"
        "test=test<<(1);"
        "test=test**(1);"
        "test=test|(1);"
        "test=test&(1);"
        "test=test%(1);"
        "delete test;"
    )
    assert functions == (
        "var test=[0,1,3,4];"
        "var tmp=test.slice(0,2);"
        "var end=test.pop();"
        "var begin=test.shift();"
        "test.unshift(begin);"
        "test.push(end);"
        "test.splice(1,2,3,3);"
        "var test='aba';"
        "test.split('b');"
        "test.substr(1,2);"
    )
    assert blocks == (
        "var test=[];"
        "var i=1;"
        "while(i<=10){"
        "test.push(i);"
        "i=i+(1);"
        "};"
        "if(test.length==10){"
        "return 'ok';"
        "}else{"
        "if(i==1){"
        "return 'oops...';"
        "}else{"
        "return 'oops...';"
        "};"
        "};"
    )


@execute
def demo_args(x, y):
    i = x
    i *= y
    return i


@execute
def demo_preprocessor(x, y):
    return x + y * x


@demo_preprocessor.preprocessor
async def preprocessor(x, y):
    return demo_preprocessor.build(x, y + 1)


@pytest.mark.asyncio
async def test_execute():
    assert demo_args.build(10, 20) == "var i=10;i=i*(20);return i;"
    assert await demo_preprocessor(7, 3) == "return 7+4*7;"
