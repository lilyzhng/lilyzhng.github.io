---
layout: page
title: Website Analytics
permalink: /analytics-demo/
description: Demonstration of different ways to display website traffic
nav: false
---

# Website Traffic Display Options

This page demonstrates different elegant ways to show website traffic on your Jekyll site.

## 1. Simple Visitor Badge

The easiest option - no signup required, just works:

{% if site.enable_hit_counter %}
<div style="text-align: center; margin: 30px 0;">
  <img src="https://hits.sh/lilyzhng.github.io.svg?style=flat-square&label=Total%20Visitors&color=4c1&labelColor=555" alt="Visitor Count" />
</div>
{% endif %}

You can customize the badge style and colors. Here are some variations:

<div style="text-align: center; margin: 20px 0;">
  <!-- Flat style -->
  <img src="https://hits.sh/lilyzhng.github.io/analytics-demo.svg?style=flat&label=Page%20Views&color=blue" alt="Page Views" style="margin: 5px;" />
  
  <!-- Plastic style -->
  <img src="https://hits.sh/lilyzhng.github.io/analytics-demo.svg?style=plastic&label=Visitors&color=success" alt="Visitors" style="margin: 5px;" />
  
  <!-- For-the-badge style -->
  <img src="https://hits.sh/lilyzhng.github.io/analytics-demo.svg?style=for-the-badge&label=Views&color=ff69b4" alt="Views" style="margin: 5px;" />
</div>

## 2. GoatCounter Integration

{% if site.goatcounter.site_id and site.goatcounter.site_id != "" %}
<div style="background: #f5f5f5; padding: 20px; border-radius: 8px; margin: 20px 0;">
  <h3>Live Visitor Count</h3>
  <p class="goatcounter-visitors" style="font-size: 24px; font-weight: bold; color: #4c1;">Loading...</p>
  <p>View detailed analytics at <a href="https://{{ site.goatcounter.site_id }}.goatcounter.com" target="_blank">GoatCounter Dashboard</a></p>
</div>
{% else %}
<div style="background: #fff3cd; padding: 20px; border-radius: 8px; margin: 20px 0;">
  <p><strong>GoatCounter not configured.</strong> To enable:</p>
  <ol>
    <li>Sign up for free at <a href="https://goatcounter.com" target="_blank">goatcounter.com</a></li>
    <li>Add your site ID to <code>_config.yml</code>:
      <pre style="background: #f8f9fa; padding: 10px; margin: 10px 0;"><code>goatcounter:
  site_id: "your-site-name"
  show_count: true</code></pre>
    </li>
  </ol>
</div>
{% endif %}

## 3. Custom Analytics Widget

You can create custom widgets to display your analytics data:

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 30px 0;">
  <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 12px; text-align: center;">
    <h3 style="margin: 0; font-size: 16px; opacity: 0.9;">Today's Visitors</h3>
    <p style="font-size: 32px; font-weight: bold; margin: 10px 0;">127</p>
    <p style="margin: 0; font-size: 14px; opacity: 0.8;">↑ 12% from yesterday</p>
  </div>
  
  <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; padding: 20px; border-radius: 12px; text-align: center;">
    <h3 style="margin: 0; font-size: 16px; opacity: 0.9;">Page Views</h3>
    <p style="font-size: 32px; font-weight: bold; margin: 10px 0;">1,843</p>
    <p style="margin: 0; font-size: 14px; opacity: 0.8;">This week</p>
  </div>
  
  <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white; padding: 20px; border-radius: 12px; text-align: center;">
    <h3 style="margin: 0; font-size: 16px; opacity: 0.9;">Avg. Duration</h3>
    <p style="font-size: 32px; font-weight: bold; margin: 10px 0;">2:34</p>
    <p style="margin: 0; font-size: 14px; opacity: 0.8;">Per session</p>
  </div>
</div>

<p style="text-align: center; color: #666; font-style: italic;">Note: These are example values. Connect to your analytics provider to display real data.</p>

## 4. Minimalist Counter

For a more subtle approach:

<div style="margin: 30px 0; text-align: center;">
  <p style="color: #666; font-size: 14px;">
    <span style="font-weight: 500;">👁️ 1,234</span> visitors this month • 
    <span style="font-weight: 500;">📈 5,678</span> total views
  </p>
</div>

## Implementation Guide

### Option 1: Simple Hit Counter (Recommended for Quick Start)
1. Already enabled in `_config.yml`
2. Add this to any page: `{% include visitor_counter.html %}`

### Option 2: GoatCounter (Recommended for Privacy)
1. Sign up at [goatcounter.com](https://goatcounter.com)
2. Update `_config.yml` with your site ID
3. Analytics will start collecting automatically

### Option 3: Google Analytics (Most Features)
1. Get tracking ID from [Google Analytics](https://analytics.google.com)
2. Enable in `_config.yml`:
   ```yaml
   enable_google_analytics: true
   google_analytics: "UA-XXXXXXXXX-X"
   ```

### Option 4: Plausible (Premium Privacy-Focused)
1. Sign up at [plausible.io](https://plausible.io)
2. Add configuration to `_config.yml`
3. Embed public dashboard if desired

---

## Tips for Elegant Display

1. **Keep it Simple**: Don't overwhelm visitors with too many metrics
2. **Match Your Theme**: Use colors and styles that fit your site design
3. **Consider Privacy**: Choose privacy-friendly options like GoatCounter or Plausible
4. **Performance**: Lightweight solutions won't slow down your site
5. **Placement**: Footer or sidebar are common locations for counters
