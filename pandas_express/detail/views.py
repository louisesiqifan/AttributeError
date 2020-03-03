from django.shortcuts import render
from django.http import HttpResponse


def detail(request):
    html = '''
    <html>
        <link rel="stylesheet" type="text/css" href="../static/detail.css">
        <link href="https://fonts.googleapis.com/css?family=Quicksand:300,500" rel="stylesheet">
        <meta name="viewport" content="width=device-width, initial-scale=0.67">
        <head>
            <title>Fairy Wing Ice Cream</title>
            <link rel="stylesheet" type="text/css" href="{% static "/detail.css" %}" />
        </head>
        <body>
            <div id="header">
                <h1>Fairy Wing Ice Cream</h1>
            </div>

            <div id="time">
                <p>Total time: 375 min</p>
            </div>

            <div id="ingredient">

            </div>

            <div id="direction">
                <h3> Direction: </h3>
                <ul>
                    <li> Whisk together the condensed milk, vanilla and salt in a large bowl; set aside. </li>
                    <li> Whip the cream until soft peaks form. Fold about 1 cup of the whipped cream into the condensed milk mixture with a rubber spatula until combined, then fold the lightened mixture into the whipped cream until well blended. </li>
                    <li> Divide 3 tablespoons of the mixture among 3 espresso cups. Tint these with pink, blue and purple food coloring. Tint the remaining mixture with yellow food coloring. Pour the yellow-tinted mixture into a chilled 9-by-5-by-3-inch metal loaf pan. Add the pink, blue and purple mixtures and swirl together. Freeze, covered, until solid and scoopable, about 6 hours. </li>
                    <li> Line a baking sheet with parchment. Put the glitter on a small plate or shallow bowl. Dip the rims of the ice cream cones into the candy melts, then dip in the glitter. Allow to set, about 15 minutes. Divide the remaining melted candy into piping bags fitted with small round tips. Pipe 12 wings onto the prepared baking sheet in pairs, one left and one right. Begin by piping an outline, extending the part where the wing will attach to the ice cream. Fill in the outlines with piped candy melts in the colors of your choice, swirling them together with a toothpick once you're done. Chill in the refrigerator to set, about 5 minutes. </li>
                    <li> Scoop a ball of ice cream onto a decorated cone and push 2 wings into opposite sides of the scoop. Add a small piece of gold leaf to the ice cream for shimmer and sparkle if desired. Repeat with the remaining ice cream cones and decorations.</li>
            </div>
            <div id="footer">
                 <h2>Presented by Team AttributeError</h2>
            </div>
        </body>
    </html>
    '''
    return HttpResponse(html)