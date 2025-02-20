---
layout: default
---

Thanks for visiting my portfolio! What will follow is a rough outline of the various aspects of my hands-on learning & experience in the realm of cyberecurity - this **is not meant to be comprehensive**, but rather to highlight & quantify some of the tangible skills and techniques that I've practiced. I currently hold, among others, active Security+ and Network+ certifications from CompTIA (which hopefully verify at least some level of foundational knowledge), so the projects here will likely be more technical and role-specific as opposed to generalized knowledge. 


# TryHackMe - SOC Level 1

![THM SOCL1 Icon](TryHackMe SOC L1 Icon.png)

The first role-specific labs I'll be documenting will come from TryHackMe's SOC Level 1 learning path & certificate! 

## Module 1. Intro

Right off the bat and from the very first module, they have us using a simplified, mock SIEM to identify a malicious connection attempt, use a mock open-source IP address database to determine if the IP is known to be malicious, escalate the alert to the correct team member (in this case, the SOC Team Lead) and then block the IP address in the firewall once given permission to do so.

See photos below:

![SIEM](TryHackMe SIEM 1.png)

![IP Check](TryHackMe OS Database IP Checking 1.png)

And the questions + answers:

![Q+A](THM Module 1 Q+A.png)


## Module 2. Pyramid of Pain

Next up is the Pyramid of Pain - this is essentially a framework that demonstrates how certain IoCs are more troubling to a threat actor than another, and is used to enhance Cyber Threat Intelligence (CTI) in many cybersecurity solutions. From AttackIQ: "The Pyramid of Pain ... provides an ascending priority list of indicators against which security controls should be applied." So, starting from the bottom and working up:

### Trivial - Hash Values

Hash values are exceptionally easy for a threat actor to circumvent, as modifying a file by even a single bit and then recompiling will produce a different hash and therefore entirely sidestep an attempted control at this level. See below for given example:

![Hash Example](THM Mod 2 - Hash.png)

### Easy - IP Address

IP addresses are also quite easy for even less experienced adversaries to work around. Blocking or denying inbound traffic/requests from a given IP is not a bulletproof defense, despite being a common (and still useful) defense tactic. We are then given an example of how threat actors can work around a control at this level, and provided static reports from [any.run](https://any.run/) to analyze and then answer the following:

![IP Example](THM Mod 2 - IP + FastFlux.png)


Text can be **bold**, _italic_, ~~strikethrough~~ or `keyword`.

[Link to another page](./another-page.html).

There should be whitespace between paragraphs.

There should be whitespace between paragraphs. We recommend including a README, or a file with information about your project.

# Header 1

This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

## Header 2

> This is a blockquote following a header.
>
> When something is important enough, you do it even if the odds are not in your favor.

### Header 3

```js
// Javascript code with syntax highlighting.
var fun = function lang(l) {
  dateformat.i18n = require('./lang/' + l)
  return true;
}
```

```ruby
# Ruby code with syntax highlighting
GitHubPages::Dependencies.gems.each do |gem, version|
  s.add_dependency(gem, "= #{version}")
end
```

#### Header 4

*   This is an unordered list following a header.
*   This is an unordered list following a header.
*   This is an unordered list following a header.

##### Header 5

1.  This is an ordered list following a header.
2.  This is an ordered list following a header.
3.  This is an ordered list following a header.

###### Header 6

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |

### There's a horizontal rule below this.

* * *

### Here is an unordered list:

*   Item foo
*   Item bar
*   Item baz
*   Item zip

### And an ordered list:

1.  Item one
1.  Item two
1.  Item three
1.  Item four

### And a nested list:

- level 1 item
  - level 2 item
  - level 2 item
    - level 3 item
    - level 3 item
- level 1 item
  - level 2 item
  - level 2 item
  - level 2 item
- level 1 item
  - level 2 item
  - level 2 item
- level 1 item

### Small image

![Octocat](https://github.githubassets.com/images/icons/emoji/octocat.png)

### Large image


### Definition lists can be used with HTML syntax.

<dl>
<dt>Name</dt>
<dd>Godzilla</dd>
<dt>Born</dt>
<dd>1952</dd>
<dt>Birthplace</dt>
<dd>Japan</dd>
<dt>Color</dt>
<dd>Green</dd>
</dl>

```
Long, single-line code blocks should not wrap. They should horizontally scroll if they are too long. This line should be long enough to demonstrate this.
```

```
The final element.
```
