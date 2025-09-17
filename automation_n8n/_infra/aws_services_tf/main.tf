provider "aws" {
    region = "us-west-2"
}

resource "aws_s3_bucket" "e_articles_bucket" {
    bucket = "e-articles-2025-september"

    tags = {
        Name        = "EArticlesBucket"
        Environment = "Dev"
    }
}