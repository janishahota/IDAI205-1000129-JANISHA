<html>
<head>
<title>Sastorytelling.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cf8e6d;}
.s1 { color: #bcbec4;}
.s2 { color: #bcbec4;}
.s3 { color: #7a7e85;}
.s4 { color: #6aab73;}
.s5 { color: #2aacb8;}
</style>
</head>
<body bgcolor="#1e1f22">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
Sastorytelling.py</font>
</center></td></tr></table>
<pre><span class="s0">import </span><span class="s1">pandas </span><span class="s0">as </span><span class="s1">pd</span>

<span class="s0">def </span><span class="s1">clean_instagram_data</span><span class="s2">(</span><span class="s1">file_path</span><span class="s2">, </span><span class="s1">save_path</span><span class="s2">):</span>
    <span class="s3"># Load dataset with correct encoding and explicit dtype handling</span>
    <span class="s1">df </span><span class="s2">= </span><span class="s1">pd</span><span class="s2">.</span><span class="s1">read_csv</span><span class="s2">(</span><span class="s1">file_path</span><span class="s2">, </span><span class="s1">encoding</span><span class="s2">=</span><span class="s4">&quot;ISO-8859-1&quot;</span><span class="s2">, </span><span class="s1">dtype</span><span class="s2">=</span><span class="s1">str</span><span class="s2">, </span><span class="s1">low_memory</span><span class="s2">=</span><span class="s0">False</span><span class="s2">)</span>

    <span class="s3"># Remove leading/trailing spaces from column names</span>
    <span class="s1">df</span><span class="s2">.</span><span class="s1">columns </span><span class="s2">= </span><span class="s1">df</span><span class="s2">.</span><span class="s1">columns</span><span class="s2">.</span><span class="s1">str</span><span class="s2">.</span><span class="s1">strip</span><span class="s2">()</span>

    <span class="s3"># Drop duplicate rows</span>
    <span class="s1">df </span><span class="s2">= </span><span class="s1">df</span><span class="s2">.</span><span class="s1">drop_duplicates</span><span class="s2">()</span>

    <span class="s3"># Handle missing values (fill forward method)</span>
    <span class="s1">df</span><span class="s2">.</span><span class="s1">ffill</span><span class="s2">(</span><span class="s1">inplace</span><span class="s2">=</span><span class="s0">True</span><span class="s2">)</span>

    <span class="s3"># Convert numerical columns to appropriate types</span>
    <span class="s1">numeric_cols </span><span class="s2">= [</span>
        <span class="s4">&quot;Impressions&quot;</span><span class="s2">, </span><span class="s4">&quot;From Home&quot;</span><span class="s2">, </span><span class="s4">&quot;From Hashtags&quot;</span><span class="s2">, </span><span class="s4">&quot;From Explore&quot;</span><span class="s2">, </span><span class="s4">&quot;From Other&quot;</span><span class="s2">,</span>
        <span class="s4">&quot;Saves&quot;</span><span class="s2">, </span><span class="s4">&quot;Comments&quot;</span><span class="s2">, </span><span class="s4">&quot;Shares&quot;</span><span class="s2">, </span><span class="s4">&quot;Likes&quot;</span><span class="s2">, </span><span class="s4">&quot;Profile Visits&quot;</span><span class="s2">, </span><span class="s4">&quot;Follows&quot;</span>
    <span class="s2">]</span>
    <span class="s1">df</span><span class="s2">[</span><span class="s1">numeric_cols</span><span class="s2">] = </span><span class="s1">df</span><span class="s2">[</span><span class="s1">numeric_cols</span><span class="s2">].</span><span class="s1">apply</span><span class="s2">(</span><span class="s1">pd</span><span class="s2">.</span><span class="s1">to_numeric</span><span class="s2">, </span><span class="s1">errors</span><span class="s2">=</span><span class="s4">'coerce'</span><span class="s2">)</span>

    <span class="s3"># Calculate total impressions</span>
    <span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Total Impressions&quot;</span><span class="s2">] = </span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;From Home&quot;</span><span class="s2">] + </span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;From Hashtags&quot;</span><span class="s2">] + </span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;From Explore&quot;</span><span class="s2">] + </span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;From Other&quot;</span><span class="s2">]</span>

    <span class="s3"># Calculate percentage of each source</span>
    <span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Home %&quot;</span><span class="s2">] = (</span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;From Home&quot;</span><span class="s2">] / </span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Total Impressions&quot;</span><span class="s2">]) * </span><span class="s5">100</span>
    <span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Hashtags %&quot;</span><span class="s2">] = (</span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;From Hashtags&quot;</span><span class="s2">] / </span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Total Impressions&quot;</span><span class="s2">]) * </span><span class="s5">100</span>
    <span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Explore %&quot;</span><span class="s2">] = (</span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;From Explore&quot;</span><span class="s2">] / </span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Total Impressions&quot;</span><span class="s2">]) * </span><span class="s5">100</span>
    <span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Other %&quot;</span><span class="s2">] = (</span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;From Other&quot;</span><span class="s2">] / </span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Total Impressions&quot;</span><span class="s2">]) * </span><span class="s5">100</span>

    <span class="s3"># Calculate engagement rates using the original Impressions column</span>
    <span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Like Rate&quot;</span><span class="s2">] = (</span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Likes&quot;</span><span class="s2">] / </span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Impressions&quot;</span><span class="s2">]) * </span><span class="s5">100</span>
    <span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Follow Rate&quot;</span><span class="s2">] = (</span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Follows&quot;</span><span class="s2">] / </span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Impressions&quot;</span><span class="s2">]) * </span><span class="s5">100</span>
    <span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Comment Rate&quot;</span><span class="s2">] = (</span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Comments&quot;</span><span class="s2">] / </span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Impressions&quot;</span><span class="s2">]) * </span><span class="s5">100</span>
    <span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Share Rate&quot;</span><span class="s2">] = (</span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Shares&quot;</span><span class="s2">] / </span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Impressions&quot;</span><span class="s2">]) * </span><span class="s5">100</span>
    <span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Save Rate&quot;</span><span class="s2">] = (</span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Saves&quot;</span><span class="s2">] / </span><span class="s1">df</span><span class="s2">[</span><span class="s4">&quot;Impressions&quot;</span><span class="s2">]) * </span><span class="s5">100</span>

    <span class="s3"># Save cleaned dataset</span>
    <span class="s1">df</span><span class="s2">.</span><span class="s1">to_csv</span><span class="s2">(</span><span class="s1">save_path</span><span class="s2">, </span><span class="s1">index</span><span class="s2">=</span><span class="s0">False</span><span class="s2">)</span>
    <span class="s1">print</span><span class="s2">(</span><span class="s4">f&quot;✅ Data cleaning complete! Saved as '</span><span class="s0">{</span><span class="s1">save_path</span><span class="s0">}</span><span class="s4">'.&quot;</span><span class="s2">)</span>

    <span class="s0">return </span><span class="s1">df</span>

<span class="s3"># Example usage</span>
<span class="s1">cleaned_df </span><span class="s2">= </span><span class="s1">clean_instagram_data</span><span class="s2">(</span><span class="s4">&quot;/Users/hota/Downloads/Instagram data.csv&quot;</span><span class="s2">, </span><span class="s4">&quot;/Users/hota/Downloads/cleaned_instagram_data.csv&quot;</span><span class="s2">)</span>
</pre>
</body>
</html>