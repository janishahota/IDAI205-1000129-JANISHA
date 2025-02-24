# Scenario 2: Likes, Comments, and Aesthetics – Analyzing Instagram Trends and Engagement Metrics

## Student Information
**Student ID:** 1000129  
**Name:** Janisha Hota  
**School:** Delhi Public School Bangalore North  
**Email:** janishahota@gmail.com  

## Introduction
> "Social media is about sociology and psychology more than technology." - Brian Solis  
This insight underscores the fundamental role that human behavior plays in shaping engagement on platforms like Instagram. As the platform continues to evolve, businesses and influencers must adjust their strategies to stay relevant and maximize audience interaction.

This document presents a systematic approach to assessing Instagram engagement using Tableau. It delves into key factors such as audience preferences, engagement trends, and content optimization strategies. By evaluating likes, comments, hashtag impact, and conversion rates, we aim to uncover actionable insights that help improve visibility and follower retention.

---

## Define the Purpose and Understand the Audience

### Purpose
- **Understanding Content Discovery Patterns:**  
  Evaluating how users encounter content—whether through Home, Hashtags, Explore, or Other sources—enables GramGaze to refine content distribution strategies and maximize reach in the most impactful areas.
- **Analyzing Engagement Patterns:**  
  By examining the distribution of Likes, Shares, Comments, and Follows, we can determine which interaction metrics drive the most engagement. Recognizing these patterns allows GramGaze to tailor content for higher audience participation.
- **Optimizing Hashtag Strategy:**  
  Assessing the effectiveness of hashtags based on engagement metrics helps identify which tags generate the highest visibility and interaction. Using high-performing hashtags strategically can enhance content reach and attract new followers.
- **Enhancing Profile Conversion Rates:**  
  Evaluating the ratio of profile visits to follows provides insight into how well content encourages new user engagement. Refining content and profile presentation can help GramGaze strengthen its online community and increase follower growth.

### Audience
- **Marketing Professionals & Brands:**  
  Businesses seeking to optimize their Instagram marketing efforts require detailed insights into engagement patterns, post performance, and audience reach. GramGaze provides data-driven recommendations to enhance brand visibility and maximize ROI.
- **Influencers & Content Creators:**  
  Understanding content engagement trends enables influencers to fine-tune their content strategies for better visibility and follower interaction. Insights into hashtag efficiency and post-performance help shape a more effective content calendar.
- **Data Analysts & Social Media Researchers:**  
  Researchers exploring Instagram engagement trends can utilize this analysis to study behavioral patterns and industry shifts. The Tableau dashboard serves as a data-driven tool for optimizing content strategies and engagement practices.

---

## Existing Analysis
To provide a comprehensive background, the following report outlines key methodologies in Instagram data analysis. It serves as a foundational guide to evaluating influencer reach and engagement on the platform.  
[[Research Report](https://iajit.org/PDF/Vol%2018%2C%20No.%201/19395.pdf)](https://iajit.org/PDF/Vol%2018%2C%20No.%201/19395.pdf)

---

## Collect and Prepare the Data
The dataset used in this project includes Instagram engagement metrics such as likes, comments, shares, follows, hashtags, and various sources of reach (Home, Explore, Hashtags, etc.). These metrics provide a comprehensive view of how posts perform on the platform.

### Data Preprocessing Steps:
- **Remove leading/trailing spaces from column names**
  <img width="284" alt="Screenshot 2025-02-25 at 4 40 16 am" src="https://github.com/user-attachments/assets/2a713be4-2688-4341-8937-d673543a5d5f" />

-  **Drop duplicate rows:** Duplicate entries were identified and removed to prevent skewed analysis.
  <img width="204" alt="Screenshot 2025-02-25 at 4 40 50 am" src="https://github.com/user-attachments/assets/e9096216-ed87-49c9-8f72-6dde61cb8aa9" />

-  **Handle missing values (fill forward method):**
  <img width="177" alt="Screenshot 2025-02-25 at 4 47 11 am" src="https://github.com/user-attachments/assets/e8b0a954-c831-4ece-8f77-f919295eeb26" />

-  **Convert numerical columns to appropriate types:** Structured for easy integration into Tableau
  <img width="631" alt="Screenshot 2025-02-25 at 4 47 23 am" src="https://github.com/user-attachments/assets/a506c2d6-b2e7-45db-b67f-b7253e6c9e63" />

-  **Calculate total impressions and percentage of each source (Data Normalisation):** The From Home, Hashtags, Explore and Other were converted into percentages, to make analysis easier.
<img width="808" alt="Screenshot 2025-02-25 at 4 48 13 am" src="https://github.com/user-attachments/assets/f0d5b23e-c5fc-43cd-8332-3c95be0f6f74" />


-  **Calculate engagement rates using the original Impressions column:** The Like, Share, Save, Follow, Comment numbers were turned into rates for easier analysis
  <img width="558" alt="Screenshot 2025-02-25 at 4 48 29 am" src="https://github.com/user-attachments/assets/6b57d83d-f766-43b1-9e66-886c212c8d44" />

-  **Save cleaned dataset:** Data was saved as a CSV for easy integration into Tableau.
<img width="492" alt="Screenshot 2025-02-25 at 4 48 41 am" src="https://github.com/user-attachments/assets/2971c8e4-1dfa-4918-b40c-1551c9793090" />



---

## Explore and Analyze the Data

### Channels of Reach
A crucial aspect of Instagram performance is how users discover content. This analysis aims to determine the primary sources of reach, such as Home, Explore, and Hashtags, and their relative contributions to overall visibility.

#### Analysis Approach: 

### Engagement Metrics
Engagement is a vital measure of content effectiveness, reflecting how users interact with posts through likes, comments, shares, and follows. This phase aims to distinguish the factors influencing engagement levels and compare content types based on interaction rates.

#### Analysis Approach: 

### Hashtag Performance
Hashtags play a critical role in expanding post reach and increasing engagement. The objective of this analysis is to identify trends in hashtag effectiveness, recognize high-performing hashtags, and explore their role in maximizing content visibility.

#### Analysis Approach: 

### Profile Visit-to-Follow Conversion Rate
A key performance indicator for growth on Instagram is the ability to convert profile visits into new followers. This study aims to evaluate the relationship between content performance and conversion rates, understand trends in follower acquisition, and identify content strategies that contribute to audience growth.

#### Analysis Approach: 

---

## Design the Visuals
To effectively present insights from the Instagram dataset, we will use a range of visualizations that make it easy to understand content trends, engagement patterns, and geographic reach. These visuals will help brands and advertisers optimize their influencer marketing strategies.

### Visualizations and Interactive Features:
- **Reach Analysis**
  <img width="1050" alt="Screenshot 2025-02-25 at 5 00 48 am" src="https://github.com/user-attachments/assets/ab6eecda-ee1d-4a71-a7f7-7f42f3a846ab" />
  
  - The highest reach comes from Home and Explore, with hashtags playing a significant role in discoverability.
  - Posts optimized for Explore and Hashtags tend to have higher visibility.
    
- **Engagement Metrics Distribution**
  <img width="1046" alt="Screenshot 2025-02-25 at 5 01 28 am" src="https://github.com/user-attachments/assets/0d490a4d-7ef5-4c3f-a0ef-3c4fb79dab31" />

  - Likes and comments show a positive correlation with shares and follows.
  - Visual content with engaging captions leads to higher interaction rates.
  - Posts with interactive elements (polls, Q&A, giveaways) receive significantly higher engagement.
 

- **Hashtag Performance**
  <img width="1044" alt="Screenshot 2025-02-25 at 5 02 02 am" src="https://github.com/user-attachments/assets/326397e8-cf7e-4de5-adae-209c32247743" />

  - Trending and niche-specific hashtags drive higher impressions.
  - Overuse of generic hashtags results in lower engagement.
  - Strategic hashtag selection improves reach and discoverability.
    
- **Profile Visit to Follows Conversion Rate**
  <img width="1049" alt="Screenshot 2025-02-25 at 5 02 27 am" src="https://github.com/user-attachments/assets/f69ab37d-d53c-49ee-8bcc-9f701428cbbb" />

  - Higher engagement posts (polls, questions) lead to an increase in profile visits.
  - Posts with strong CTA (Call-to-Action) convert visitors into followers at a higher rate.

---

## Storyboard In Tableau




**[Storyboard Created Using Canva](https://www.canva.com/)**

---
## Add Context and Annotations
Explain Insights: Use annotations to describe the relationships between reach, engagement metrics, and hashtag performance, helping users understand the implications of each metric.
Contextual Information: Provide background information on how GramGaze can leverage these insights to optimise future Instagram strategies.


---
## Test the Dashboard
Publish: Publish the interactive Tableau dashboard allowing to explore insights into Instagram trends.
Actionable Insights: Provide with recommendations based on the dashboard’s findings in storyboard, such as optimising content for specific reach sources or hashtag usage.
---

## Conclusion
### Strengths:
- The project provides valuable insights into Instagram engagement and trends.
- Data-driven recommendations help optimize content strategies.
- Tableau visualizations make trends easy to interpret.

### Future Scope:
- Use A/B testing to analyze the impact of different post captions on engagement.
- Incorporate AI-driven hashtag recommendations.
- Analyze the impact of posting time on engagement.

---

## Resources:
1. **Storyboard:** [Canva](https://www.canva.com/)
2. **Visualizations:** [Tableau Public](https://public.tableau.com/app/discover)
3. **Data Cleaning and Preprocessing:** Python

---

## Bibliography
-https://improvado.io/blog/instagram-analytics-dashboard
-https://public.tableau.com/app/profile/tinu6387/viz/Instagramtrends/InstagramTrends
-https://medium.com/@mahishag/data-analysis-using-excel-71d1c773fcf9
-https://help.tableau.com/current/pro/desktop/en-us/viewparts_marks_markproperties_color.htm
-https://inflact.com/tools/profile-analyzer/
-chatgpt.com
-https://www.kaggle.com/code/muliasujiastuti/instagram-reach-analysis
-https://brandmentions.com/hashtag-tracker/

