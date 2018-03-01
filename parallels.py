from Workload import FileHandler
import time
def main():
    urls = ["http://www.in.gr",
            "http://www.zougla.gr",
            "https://www.aueb.gr",
            "http://tainies.gr",
            "http://www.veggos.gr",
            "http://www.alpha.gr"]
    fh = FileHandler()
    fh.seturls(urls)
    start_time = time.time()

    #fh.start()
    fh.start_multiproc(4)
    fh.print_results()
    end_time = time.time()
    print("Time: %ssecs" % (end_time - start_time))
main()