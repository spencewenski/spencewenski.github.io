---
layout: post
title:  "Add Reminder Button"
date: 2016-04-13
categories:
- programming
tags:
- programming
---

I used to use Google reminders all the time, but I haven't recently because I
became infuriated by the totally inefficient and tedious process of getting to
the add reminder page of the Google app (four whole taps!). There has to be a
better and faster way to create reminders, ideally with a single tap. Luckily,
I'm a developer (though not a very experienced Android developer, if I'm being
honest), so even if Google can't provide the ideal experience, I can create it
for myself.

<!--more-->

The easiest and probably simplest solution to my problem is to create a stub app
that just opens the Google app with the query 'add reminder'. So, that's exactly
what I did.

In addition, I use this app with the [Nova Launcher][nova-launcher] which allows
me to 1) launch the app with a gesture to reduce clutter on my home screen and
2) hide the app from my app drawer to reduce clutter in my app drawer.

The full project can be found on GitHub [here][project-url], and
here's the code for the main activity:

{% highlight java %}
public class MainActivity extends AppCompatActivity {

    public static final String ADD_REMINDER = "add reminder";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        launchGoogleSearch(ADD_REMINDER);
    }

    @Override
    protected void onStart() {
        super.onStart();
        launchGoogleSearch(ADD_REMINDER);
    }

    /**
     * Launch a Google Search activity with the given query
     *
     * If the query starts with 'http' or 'https', launches a search in a web browser;
     * otherwise, Google search will be applied
     *
     * https://developer.android.com/reference/android/content/Intent.html#ACTION_WEB_SEARCH
      */
    private void launchGoogleSearch(String query) {
        Intent intent = new Intent(Intent.ACTION_WEB_SEARCH);
        intent.putExtra(SearchManager.QUERY, query);
        startActivity(intent);
    }
}
{% endhighlight %}


[project-url]: https://github.com/spencewenski/AddReminderButton
[nova-launcher]: http://novalauncher.com/