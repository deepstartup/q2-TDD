import trace, sys

# Test Code : Test case coverage

if __name__ == "__main__":
    t = trace.Trace(ignoredirs=[sys.prefix, sys.exec_prefix], count=1, trace=0)
    t.runfunc(unittest.main)
    r = t.results()
    r.write_results(show_missing=True)