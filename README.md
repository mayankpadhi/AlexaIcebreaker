# Alexa with Nice Icebreaker skill

## Introduction

This is an alexa skill which gives you a nice icebreaker when you ask for it. You can use it to initiate a conversation or a discussion with people around you. It was featured in hasura [hub](https://hasura.io/hub/projects/mayankpadhi/alexa-nice-icebreaker)

## How does it work?

### Workflow
You can test out this skill using an Amazon Echo device or at [Echosim](https://echosim.io). The workflow is as follows:
- You invoke the skill saying "Alexa, start Nice Icebreaker."
- Alexa will give you a nice icebreaker and ask if you want more.
- If you say yes, it would again give you a nice icebreaker and ask if you want more. If you say no, it will exit out of the skill.

### Internal Implementation

This skill is written in Python using Flask and the python library [Flask-Ask](https://github.com/johnwheeler/flask-ask). The Implementation is as follows:
- When you invoke the skill, one of the four functions is called:
    * Latest Indian Entertainment News.
    * Latest Indian Sports News.
    * A "This Day in History" fact.
    * A number trivia.

- The output of the function is spoken out by Alexa along with a question if you want more nice icebreaker.
- If you say yes, first step repeats.
- If you say no, Alexa echoes "Bye" and exits out of the skill.

## How to get it up and running?

### Deployment
This skill gets deployed instantly. Also, Hasura automatically generates SSL certificates for you. Just run the following commands to deploy your skill.

(Make sure you have [hasura-cli](https://docs.hasura.io/0.15/manual/install-hasura-cli.html))

```
$ hasura quickstart mayankpadhi/alexa-icebreaker
$ cd alexa-icebreaker
$ git add . && git commit -m "Initial Commit"
$ git push hasura master
```

### How to add the skill to your Amazon account?

To link it with your Amazon Echo Device, go to your [Amazon developer console](https://developer.amazon.com/edw/home.html#/skills).

1. Create a new skill. Call it `Nice Icebreaker`. Give the invocation name as `nice icebreaker`. Click next.

2. Add this intent schema

```
{
  "intents": [
    {
      "intent": "YesIntent"
    },
    {
      "intent": "NoIntent"
    }
  ]
}
```

Leave custom slot types empty. Add the following sample utterances

```
YesIntent yes
YesIntent sure
YesIntent yeah
YesIntent ok

NoIntent no
NoIntent no thanks
NoIntent nope
```

   Click next.

3. For the service endpoint, check the `HTTPS` radio button.

	Put the default URL as `https://bot.<cluster-name>.hasura-app.io/yoda_quotes`. (Run `$ hasura cluster status` from root directory to know your cluster name).

	**Note**: For quick testing, we have one skill service live at https://bot.brawl60.hasura-app.io/yoda_quotes. (This test service will work only if you have followed 1 and 2)

	Click next.

4. About SSL certificates, Hasura services have auto generated `LetsEncrypt` Grade A SSL certificates. This means, you have to check the radio button that says `My development endpoint has a certificate from a trusted certificate authority`

	Click next.

5. Your skill is live on the ECHO device associated with your account. Test it by saying **Alexa**, `load nice icebreaker`. And Alexa will give you nice *Icebreaker* :)
