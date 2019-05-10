class VcfReader:
	# constructor
    def __init__(self, fname):
        self.fname = fname
        self.flines = [x.strip() for x in open(fname)]
        self.file_header = [l for l in self.flines if l.startswith('##')]
        self.column_header = [l.split() for l in self.flines if l.startswith('#') and not l.startswith("##")][0]
        self.lines = [x.split() for x in self.flines if not x.startswith('#')]

    def get_chrom(self, chr):
        chr = str(chr)
        return [x for x in self.lines if x[0] == chr]

    def __str__(self):
        return self.fname

    def __len__(self):
        return len(self.flines)

    vr = VcfReader('example.vcf')
    header = vr.file_header
    column_header = vr.column_header
    line = vr.lines
    # print((vr.column_header))
