from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Post(models.Model):
    """
    Model representing a blog post.

    Fields:
    - title: Title of the post (unique).
    - slug: Slug for URL usage (unique).
    - author: The user who wrote the post.
    - featured_image: The main image associated with the post (stored in Cloudinary).
    - content: Main content of the post.
    - created_on: Date and time when the post was created.
    - status: Status of the post (Draft/Published).
    - excerpt: Short excerpt of the post, optional.
    - updated_on: Date and time when the post was last updated.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.CharField(max_length=500, blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta class to define the ordering of the post list.
        Orders by created_on date in descending order and then by author.
        """
        ordering = ['-created_on', 'author']
        

    def __str__(self):
        """
        String representation of the Post model, returns title and author.
        """
        return f"{self.title} written by {self.author}"


class Comment(models.Model):
    """
    Model representing a comment on a blog post.

    Fields:
    - post: The blog post related to the comment.
    - author: The user who wrote the comment.
    - body: The content of the comment.
    - approved: Whether the comment has been approved by the admin.
    - created_on: Date and time when the comment was created.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta class to define the ordering of comments by creation date.
        Orders by created_on date in descending order.
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        String representation of the Comment model, returns the comment body and author.
        """
        return f"Comment {self.body} by {self.author}"


class Event(models.Model):
    """
    Model representing an event.

    Fields:
    - event_name: The name of the event (unique).
    - location: The location where the event will be held.
    - date: The date and time of the event.
    """
    event_name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        """
        String representation of the Event model, returns the event name.
        """
        return self.event_name
    

class Ticket(models.Model):
    """
    Model representing a ticket for an event.

    Fields:
    - ticket_holder: The user who holds the ticket.
    - date_issued: The date when the ticket was issued.
    - event: The event for which the ticket was issued.
    """
    ticket_holder = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users_tickets"
    )
    date_issued = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="event_tickets"
    )

    def __str__(self):
        """
        String representation of the Ticket model, returns the ticket holder's information.
        """
        return f"Ticket for {self.ticket_holder}"
