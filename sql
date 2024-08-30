CREATE TABLE "domains_location" (
  "SourceCommonName" VARCHAR PRIMARY KEY,
  "location" VARCHAR(2),
  "Country" VARCHAR
);

CREATE TABLE "traffic_data" (
  "id" SERIAL PRIMARY KEY,
  "GlobalRank" INTEGER,
  "TldRank" INTEGER,
  "Domain" VARCHAR,
  "TLD" VARCHAR,
  "RefSubNets" INTEGER,
  "RefIPs" INTEGER,
  "IDN_Domain" VARCHAR,
  "IDN_TLD" VARCHAR,
  "PrevGlobalRank" INTEGER,
  "PrevTldRank" INTEGER,
  "PrevRefSubNets" INTEGER,
  "PrevRefIPs" INTEGER
);

CREATE TABLE "data" (
  "article_id" SERIAL PRIMARY KEY,
  "source_id" INTEGER,
  "source_name" VARCHAR,
  "author" VARCHAR,
  "title" TEXT,
  "description" TEXT,
  "url" TEXT,
  "url_to_image" TEXT,
  "published_at" TIMESTAMP,
  "content" TEXT,
  "category" VARCHAR,
  "article" TEXT,
  "title_sentiment" VARCHAR,
  "main_domain_extracted_From_url" VARCHAR
);

ALTER TABLE "data" ADD FOREIGN KEY ("main_domain_extracted_From_url") REFERENCES "traffic_data" ("Domain");

ALTER TABLE "data" ADD FOREIGN KEY ("source_name") REFERENCES "domains_location" ("SourceCommonName");
