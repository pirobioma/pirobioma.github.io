# The Pyrobiome of the Maule Region: a culture collection of pyrophilous fungi and bacteria (v1.0)

**Pirobioma del Maule Project** · ANID FONDECYT Initiation Grant No. 11240628
Universidad de Talca · Centro de Ecología Integrativa (Chile)
Website: https://pirobioma.github.io/ · Contact: Ian S. Acuña-Rodríguez (ian.acuna@utalca.cl)

## Overview
This dataset documents **139 culturable microbial strains (74 fungi, 65 bacteria)** isolated from
post-fire soils in the Maule Region, south-central Chile. Strains were isolated on selective media
with **burned-wood charcoal as the sole carbon source**, from soils of native Maulino forest
(*Nothofagus alessandrii* and *N. glauca*) and *Pinus radiata* plantations burned in the 2017 and
2023 megafires. Six fungal strains were isolated from mushroom fruiting bodies.

Each record includes taxonomy, soil origin, soil horizon, burn condition, a 1–5 growth score on
charcoal medium, a morphological description and the marker-gene sequence
(16S rRNA for bacteria, ITS for fungi) where available (117 of 139 strains).
Photographs of each strain (plates and stains) are available on the project website.

## Sampling design
Paired design comparing native forest and *P. radiata* plantations under three burn conditions:

| Condition | Native forest | *P. radiata* plantation |
|---|---|---|
| Unburned (control) | Pilén, El Secreto de Pilén Reserve | Empedrado municipality |
| Recently burned (~1 year) | Molco | Huaquén |
| Burned long ago (~8 years) | Los Ruiles National Reserve | Empedrado |

Soil was sampled at two horizons (topsoil and deep soil).

## Files
| File | Content |
|---|---|
| `pirobioma_catalogue.xlsx` | Full catalogue in English (sheet *Strains*) plus column definitions (sheet *Read me*) |
| `pirobioma_catalogo.xlsx` | Same catalogue in Spanish (sheets *Cepas* and *Léeme*) |
| `pirobioma_sequences.fasta` | 117 marker-gene sequences. Header: `>Code Identification \| Marker \| Method \| Soil origin \| Burn condition \| Horizon` |
| `README.md` | This file |

## Columns (catalogue)
- **Code** — strain code (B = bacterium, H = fungus), matches the FASTA header and the website record.
- **Type** — Bacterium / Fungus.
- **Identification** — name assigned from the marker-gene sequence (may be genus level or "sp.").
- **Phylum … Species** — full taxonomy.
- **Soil origin** — Native forest, Pine plantation (*P. radiata*) or Mushroom (fruiting body).
- **Horizon** — Topsoil or Deep soil.
- **Burn condition** — Recently burned (~1 year) or Burned long ago (~8 years).
- **Growth on charcoal medium (1–5)** — 1 = very little growth, 5 = abundant growth.
- **Morphological description** — colony (and, for fungi, obverse/reverse and microscopic) traits.
- **Marker / Sequencing method / Length (bp)** — 16S rRNA (primers 27F + 1492R) or ITS (ITS1 + ITS4);
  forward+reverse consensus or single read.
- **Sequence** — nucleotide sequence (5'→3').
- **Online record** — link to the strain record (photos) on the website.

Empty cells mean the data is not yet available for that strain.

## Licence
Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).
Free for non-commercial use with attribution. For commercial use, please contact ian.acuna@utalca.cl.

## How to cite
Acuña-Rodríguez IS, Ascencio Astudillo C, Barrera Valenzuela A & Miño R (2026) The Pyrobiome of the Maule Region: a culture collection of pyrophilous fungi and bacteria (FONDECYT 11240628). Version 1.0 [Data set]. Centro de Ecología Integrativa, Universidad de Talca. Zenodo. https://doi.org/10.5281/zenodo.24043372 — Online catalogue: https://pirobioma.github.io/

## Acknowledgements
ANID (FONDECYT Initiation 11240628), Universidad de Talca, Centro de Ecología Integrativa,
El Secreto de Pilén Reserve, CONAF Maule and CONAF Ñuble.
