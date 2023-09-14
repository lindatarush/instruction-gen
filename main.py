from template import Template

f = {"question": 'Whether genetics increase the risk of diabetes?',
 "instruction": '''
Give a list of genes mentioned in the provided material that are significantly associated with an increased 
risk of Type 2 Diabetes Mellitus (T2DM) due to their involvement in genetic variants and polymorphisms, and 
summarize any relevant information about their impact on diabetes risk.
''',
 "material": '''
Recently, Genome-wide association (GWAS) study, suggests the involvement of more than 50 genetic variants with
 T2DM [8]. Several genes previously observed are significantly associated with T2DM including PON1, LCAT, APOE, FTO,
 and TCF7L2[2,9]. Polymorphisms in these genes have previously been shown to be significantly associated with T2DM by 
 an increase in free fatty acid (FFA). Exposure of cells to increased FFA inhibits the phosphorylation of serine residues 
 of the insulin receptor substrate (IRS). This phosphorylation diminishes the tyrosine phosphorylation of IRS-1 in reaction 
 to insulin and loses the capability to bind with insulin receptors thus inhibiting insulin action and signaling. Mechanism 
 and causes of T2DM are mostly unknown and various polymorphic studies in different ethnicities are being conducted to identify 
 the genes responsible for the progression of diabetes [10]. However, the sequence of genes diverges in various regions, and 
 the dissimilarity in nucleotide modifies a phenotypic trait that displays an increased risk of T2DM. Apart from coding genes,
 non-coding genes can also raise the risk of diabetes by modifying the regulation of genes which alters the protein product
and functioning [11]. It has also been identified that the development of T2DM results from the involvement of genetic 
makeup and the environmental factors together with increased obesity (visceral fat). The population of different 
ethnicities is also at increased risk of diabetes such as African-Americans, Asian-Americans, and Hispanic-Americans 
[7]. However, the increase in a sedentary life, poor foodstuffs, stress, red meat, westernization culture, urbanization, 
and competition showed an increased frequency of T2DM among Indians [7]. This review will thus focus on a wide variety of
significant aspects, from genetic background to topics related to the pathogenesis of diabetes mellitus such as dysfunctional 
beta cells and lipotoxicity. There is also an inventory of presently used therapeutic tools and a review of novel therapeutic 
approaches like incretin-based therapies or sodium-glucose transporter-2 inhibitors. Additionally, providing a concise but 
comprehensive update, this review will be essential to every clinician involved in the treatment of diabetes mellitus.
''',

"input": "This is input.",
 "verb_root": "get list"}


