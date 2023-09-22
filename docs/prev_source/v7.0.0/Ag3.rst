Ag3 API
=======

This page provides a curated list of functions and properties available in the malariagen_data API relating to *Anopheles gambiae* data.

.. currentmodule:: malariagen_data.ag3.Ag3

Basic data access
-----------------
.. autosummary::
    :toctree: generated/

    pca
    plot_pca_coords
    plot_pca_coords_3d
    plot_pca_variance
    releases
    results_cache_get
    results_cache_set
    v3_wild

Sample metadata access
----------------------
.. autosummary::
    :toctree: generated/

    aim_calls
    aim_variants
    cohort_diversity_stats
    count_samples
    cross_metadata
    plot_aim_heatmap
    plot_samples_interactive_map
    sample_cohorts
    species_calls
    wgs_data_catalog

SNP data access
---------------
.. autosummary::
    :toctree: generated/

    aa_allele_frequencies
    aa_allele_frequencies_advanced
    diversity_stats
    geneset
    genome_features
    genome_sequence
    igv
    is_accessible
    open_genome
    open_site_annotations
    open_snp_genotypes
    plot_diversity_stats
    plot_heterozygosity
    plot_heterozygosity_track
    plot_frequencies_heatmap
    plot_frequencies_interactive_map
    plot_frequencies_map_markers
    plot_frequencies_time_series
    plot_genes
    plot_snps
    plot_snps_track
    plot_transcript
    resolve_region
    site_annotations
    site_filters
    snp_allele_counts
    snp_allele_frequencies
    snp_allele_frequencies_advanced
    snp_calls
    snp_dataset
    snp_effects
    snp_genotypes
    snp_variants
    snp_sites
    view_alignments


Haplotype data access
---------------------
.. autosummary::
    :toctree: generated/

    h12_calibration
    h12_gwss
    h1x_gwss
    haplotypes
    open_haplotypes
    open_haplotype_sites
    plot_h12_calibration
    plot_h12_gwss_track
    plot_h12_gwss
    plot_h1x_gwss
    plot_h1x_gwss_track
    plot_haplotype_clustering
    plot_haplotype_network
    

CNV data access
---------------
.. autosummary::
    :toctree: generated/

    cnv_coverage_calls
    cnv_discordant_read_calls
    cnv_hmm
    gene_cnv
    gene_cnv_frequencies
    gene_cnv_frequencies_advanced
    open_cnv_coverage_calls
    open_cnv_discordant_read_calls
    open_cnv_hmm
    plot_cnv_hmm_coverage
    plot_cnv_hmm_coverage_track
    plot_cnv_hmm_heatmap
    plot_cnv_hmm_heatmap_track
    plot_roh
    plot_roh_track
    roh_hmm
