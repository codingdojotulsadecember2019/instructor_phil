using System;
using Microsoft.AspNetCore.Mvc;

namespace DemoProject.Controllers
{
    public class HelloController : Controller
    {
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            return View();
        }

        [HttpGet("users/{userId}")]
        public IActionResult Show(int userId)
        {
            ViewBag.UserId = userId;
            return View();
        }

        [HttpGet("admin/{UserId}")]
        public IActionResult Admin(int UserId)
        {
            return RedirectToAction("Show", new { userId = UserId });
        }
        [HttpPost("users")]
        public IActionResult Process(string name, int age)
        {
            Console.WriteLine($"Name is: {name}");
            Console.WriteLine($"Age is: {age}");
            return RedirectToAction("Index");
        }
    }
}