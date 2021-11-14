from testbook import testbook


@testbook("./notebooks/helloworld.ipynb", execute=True)
def test_hello_world(tb):
    assert tb.cell_output_text(0) == "hello, world!"
