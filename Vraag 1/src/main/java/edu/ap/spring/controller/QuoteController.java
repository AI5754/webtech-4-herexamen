package edu.ap.spring.controller;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Set;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import edu.ap.spring.redis.RedisService;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class QuoteController {

  @Autowired
  private RedisService service;

  // @GetMapping("/eb")
  // public String getAnswer(Model model) {

  // ArrayList<String> quotes = new ArrayList<String>();
  // for (String a : this.service.keys("quote:" + authorid + ":*")) {
  // quotes.add(this.service.getKey(a));
  // }

  // String author = this.service.getKey(this.service.keys("author:*:" +
  // authorid).iterator().next());
  // model.addAttribute("quotes", quotes);
  // model.addAttribute("author", author);

  // return "listQuotes";

  // // ArrayList<String[]> answers = new ArrayList<String[]>();
  // // for (String a : this.service.keys("author:*")) {
  // // String[] parts = a.split(":");
  // // int id = Integer.parseInt(parts[parts.length - 1]);
  // // System.out.println("hi " + id);

  // // authors.add(new String[] { this.service.getKey(a), String.valueOf(id) });

  // // }
  // // model.addAttribute("authors", authors);
  // // System.out.println(authors);

  // // return "listAuthors";
  // }

  // @GetMapping("/listauthors")
  // public String listAuthors(Model model) {

  // ArrayList<String[]> authors = new ArrayList<String[]>();
  // for (String a : this.service.keys("author:*")) {
  // String[] parts = a.split(":");
  // int id = Integer.parseInt(parts[parts.length - 1]);
  // System.out.println("hi " + id);

  // authors.add(new String[] { this.service.getKey(a), String.valueOf(id) });

  // }
  // model.addAttribute("authors", authors);
  // System.out.println(authors);

  // return "listAuthors";
  // }

  // @GetMapping("/listquotes/{authorid}")
  // public String listQuotesById(@PathVariable("authorid") int authorid, Model
  // model) {

  // ArrayList<String> quotes = new ArrayList<String>();
  // for (String a : this.service.keys("quote:" + authorid + ":*")) {
  // quotes.add(this.service.getKey(a));
  // }

  // String author = this.service.getKey(this.service.keys("author:*:" +
  // authorid).iterator().next());
  // model.addAttribute("quotes", quotes);
  // model.addAttribute("author", author);

  // return "listQuotes";
  // }

  @GetMapping("/eb")
  public String getAuthorForm() {
    return "addAuthor"; // get answer
  }

  @PostMapping("/eb")
  public String addAuthor(@RequestParam("question") String question, Model model) {

    String answer;
    if (this.service.exists(question)) {
      answer = this.service.getKey(question);

    } else {
      answer = generateAnswer();
      this.service.setKey(question, answer);
    }
    model.addAttribute("question", question);
    model.addAttribute("answer", answer);
    return "answer";
  }

  private String generateAnswer() {
    List<String> answers = new ArrayList<>();
    answers.add("It is certain.");
    answers.add("It is decidedly so.");
    answers.add("Without a doubt.");
    answers.add("Yes - definitely.");
    answers.add("You may rely on it.");
    answers.add("As I see it, yes.");
    answers.add("Most likely.");
    answers.add("Outlook good.");
    answers.add("Yes.");
    answers.add("Signs point to yes.");
    answers.add("Reply hazy, try again.");
    answers.add("Ask again later.");
    answers.add("Better not tell you now.");
    answers.add("Cannot predict now.");
    answers.add("Concentrate and ask again.");
    answers.add("Don't count on it.");
    answers.add("My reply is no.");
    answers.add("My sources say no.");
    answers.add("Outlook not so good.");
    answers.add("Very doubtful.");

    List<String> answers2 = new ArrayList<>(answers);

    Random g = new Random();
    String answer = answers2.get(g.nextInt(answers2.size() - 1));
    Set<String> keys = service.keys(answer);

    boolean allUsed = false;

    while (keys.size() != 0 && !allUsed) {
      if (answers2.size() > 0) {
        answers2.remove(answer);
        answer = answers2.get(g.nextInt(answers2.size() - 1));
        keys = service.keys(answer);
      } else
        allUsed = true;
    }

    if (allUsed)
      answer = answers.get(g.nextInt(answers.size() - 1));

    return answer;
  }

  // @GetMapping("/quote")
  // public String getQuoteForm(Model model) {

  // ArrayList<String> authors = new ArrayList<String>();
  // for (String a : this.service.keys("author:*")) {
  // authors.add(this.service.getKey(a));
  // }
  // model.addAttribute("authors", authors);

  // return "addQuote";
  // }

  // @PostMapping("/quote")
  // public String addQuote(@RequestParam("quote") String quote,
  // @RequestParam("author") String author) {

  // String[] authorName = author.split(" ");
  // String authorKey = this.service.keys("author:" + authorName[0] +
  // authorName[1] + ":*").iterator().next();
  // if (this.service.exists("quotecount")) {
  // this.service.incr("quotecount");
  // } else {
  // this.service.setKey("quotecount", "1");
  // }

  // this.service.setKey("quote:" + authorKey.split(":")[2] + ":" +
  // this.service.getKey("quotecount"), quote);

  // return "redirect:listquotes/" + authorKey.split(":")[2];
  // }
}
