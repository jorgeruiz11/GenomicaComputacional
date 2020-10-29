# Comandos de la Práctica 01
## Jorge Antonio Ruiz López

# Parte I.

**Respuesta 1:**

/bin/bash

**Respuesta 2:**

mkdir data && mkdir filtered && mkdir rawdata && mkdir meta && mkdir scripts && mkdir figures && mkdir archive

**Respuesta 3:**

mv filtered/ data/ && mv raw_data/ data/


**Respuesta 4:**

La organización se debe a que es necesario separar los distintos tipos de información dependiendo de su uso.
Por ejemplo: los datos crudos en un directorio y los modificados por análisis subsecuentes en otros. Así mismo
  no es bueno mezclar la información cruda con los scripts pues debemos también facilitar el acceso a distintos
  usuarios y que sea entendible.  

# Parte II.

**Respuesta 1:**

ls -l delay.sh

chmod u+x delay.sh

**Respuesta 2:**

ls -l delay.sh

./delay.sh

**Respuesta 3:**

las líneas añadidas al archivo fueron:

sleep 30
echo "Ya puedo continuar!"

**Respuesta 4:**

./delay.sh &

[1] 10769
Después de la Parte I. necesito un descanso de exactamente 30 segundos.

kill -9 10769

# Parte III

**Respuesta 1:**

La ubicación del archivo de texto es: GenomicaComputacional/jruiz_p01/meta

**Respuesta 2:**

mv sequence.fasta sarscov2_genome.fasta && mv sequence.gff3 sarscov2_genome.gff3

**Respuesta 3:**

mv sequence.fasta splike_c.faa
mv sequence\(1\).fasta splike_b.faa
mv sequence\(2\).fasta splike_a.faa

**Respuesta 4:**

mv sarscov2_genome.fasta sarscov2_genome.gff3 splike_c.faa splike_b.faa splike_a.faa SRR10971381_R1.fastq.gz SRR10971381_R2.fastq.gz sarscov2_assembly.fasta.gz data/raw_data

# Parte IV

**Respuesta 1:**

ln -s ../raw_data/splike_c.faa splike_c.faa
ln -s ../raw_data/splike_b.faa splike_b.faa
ln -s ../raw_data/splike_a.faa splike_a.faa

**Respuesta 2:**

touch glycoproteins.faa

**Respuesta 3:**

>pdb|6VXX|C Chain C, SARS-CoV-2 spike glycoprotein
>pdb|6VXX|B Chain B, SARS-CoV-2 spike glycoprotein
>pdb|6VXX|A Chain A, SARS-CoV-2 spike glycoprotein

**Respuesta 4:**

cat splike_a.faa splike_b.faa splike_c.faa > glycoproteins.faa

**Respuesta 5:**

mv data/raw_data/splike_a.faa archive/ && mv data/raw_data/splike_b.faa archive/ && mv data/raw_data/splike_c.faa archive/

**Respuesta 6:**

cat sarscov2_genome.fasta

head -3 sarscov2_genome.fasta
>NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome
ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAA
CGAACTTTAAAATCTGTGTGGCTGTCACTCGGCTGCATGCTTAGTGCACTCACGCAGTATAATTAATAAC


Para el archivo comprimido:

cat sarscov2_assembly.fasta.gz

zless sarscov2_assembly.fasta.gz | head -3
>NODE_1_length_264_cov_161.042781
CACAAATCTTAACACTCTTCCCTACACGACGCTCTTCCGATCTACGCCGGGCCATTCGTA
CGAACCGATACCTGTGGTAAAGGGTCCTACTGTATGGTGGTACACGAGTAGTAGCAAATG


**Respuesta 7:**

grep ">" sarscov2_genome.fasta
>NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome

Respuesta: 1.

Para el archivo comprimido:

zless sarscov2_assembly.fasta.gz | grep ">"
>NODE_1_length_264_cov_161.042781
>NODE_2_length_140_cov_236.777778
>NODE_3_length_129_cov_192.884615
>NODE_4_length_29906_cov_267.734051
>NODE_5_length_78_cov_582779.000000
>NODE_6_length_88_cov_3449.454545
>NODE_7_length_88_cov_3378.545455
>NODE_8_length_103_cov_3109.346154
>NODE_9_length_92_cov_4902.000000
>NODE_10_length_92_cov_4923.266667
>NODE_11_length_78_cov_12.000000
>NODE_12_length_267_cov_0.768421
>NODE_13_length_241_cov_0.884146
>NODE_14_length_244_cov_0.868263
>NODE_15_length_262_cov_0.783784
>NODE_16_length_229_cov_0.914474
>NODE_17_length_236_cov_0.861635
>NODE_18_length_233_cov_0.865385
>NODE_19_length_234_cov_0.859873
>NODE_20_length_237_cov_0.862500
>NODE_21_length_237_cov_0.837500
>NODE_22_length_233_cov_0.858974
>NODE_23_length_230_cov_0.856209
>NODE_24_length_235_cov_0.816456
>NODE_25_length_230_cov_0.862745
>NODE_26_length_235_cov_0.803797
>NODE_27_length_256_cov_0.765363
>NODE_28_length_232_cov_0.716129
>NODE_29_length_234_cov_1.146497
>NODE_30_length_235_cov_0.759494
>NODE_31_length_277_cov_0.870000
>NODE_32_length_232_cov_1.025806
>NODE_33_length_271_cov_1.221649
>NODE_34_length_254_cov_0.757062
>NODE_35_length_236_cov_1.012579

Respuesta: 35

**Respuesta 8:**

zless SRR10971381_R2.fastq.gz | head -12@SRR10971381.512_2
CGTGGAGTATGGCTACATACTACTTATTTGATGAGTCTGGTGAGTTTAAAGTGGCTTCACATATGTATTGTTCTTTCTACCCTCCAGATGAGGATGAAGAAGAAGGTGATTGTGAAGAAGAAGAGTTTGAGCCATCAACTCAATATGAGT
+
/FFFA/A/FFFF66FFFFFF/FF/FFFFFFFFFFFFF/AFFF6FFFA6FFFFF/FFFFFFFFFFFFFFFFFF/FF/FFFFFA/FFF/FFF/A/AFA/FFFFF/=F/F/F/AFAFF//A/AFF//FFAF/FFF=FFAFFFA/A/6=///==
@SRR10971381.556_2
TTTGTAAAAATAAAATAAAAAAAATAAAAATAATATATTAAAAAAAGATAAATAAAAAAATGAACAATTAATAAAAAAAAAAAAAAAAAAAAATTAAAAAAAAAAAAAAAAAAAATAAAAAAAAAAAAAAATAAAAAAAAAATTATAAAA
+
6AFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF/FFFAFFFFFF/FFA/FF=F//=FF/FFFFFFFFFFFFFA/FFFF/FF/FA//F/FFFFFFA/=FFFFF/FFFF/F=FFFAFF///FFFFA/FF/6//////=/
@SRR10971381.1428_2
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
+
FFFFFFFFFFFFAFFFAFFFFFF6A//F//FFF

Las secuencias vecían separadas por un "+" en el archivo, así que el número de
secuencias lo obtenemos buscando el número de apariciones de "+", + 1

zless SRR10971381_R2.fastq.gz | grep -c "+"
130022

Respuesta: 130023

**Respuesta 9:**

Los .fasta contienen secuencias de proteína o ADN sin procesar con una
etiqueta que especifica cuáles son las secuencias o de dónde provienen.

Los .fastaq contienen lecturas de secuencia sin procesar producidas a
partir de un secuenciador de ADN. Estos se originan típicamente de secuenciadores
Illumina. A cada par de bases en la lectura se le asigna un puntaje de calidad
asociado (es decir, la probabilidad de que el par de bases se haya identificado
correctamente).

Los .faa son usados en NCBI para los FASTA Amino Acidos, lo que significa que
éste es un archivo de proteína FASTA.

**Respuesta 10:**

El comando less nos permite ver un archivo de texto de forma plana en la terminal, pero
no nos permite editarlo.

La diferencia con less y less -S es que el -S actua de la forma de cortar líneas, es
como si diera un formato "bonito" al texto, mientras que less lo muestra tal cual lo va leyendo

**Respuesta 11:**

awk '{print $3}' sarscov2_genome.gff3
1

region
five_prime_UTR
gene
CDS
CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
mature_protein_region_of_CDS
stem_loop
stem_loop
gene
CDS
gene
CDS
gene
CDS
gene
CDS
gene
CDS
gene
CDS
gene
CDS
gene
CDS
gene
CDS
gene
CDS
stem_loop
stem_loop
three_prime_UTR
stem_loop



awk '{print $3}' sarscov2_genome.gff3 > prueba.text
grep -c "gene" prueba.txt

11

Cantidad de genes: 11


La diferencia entre gene y CDS, CDS tiene el nombre de la proteína, miestras que
gene es un nombre que contiene las caracteristicas reelevantes y sus nombres
deben seguir las reglas de nomenclatura bacteriana estándar de tres letras minúsculas.
