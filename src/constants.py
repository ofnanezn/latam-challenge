import pyarrow as pa


USER_FIELDS = [
    pa.field("username", pa.string()),
    pa.field("displayname", pa.string()),
    pa.field("id", pa.int64()),
    pa.field("description", pa.string()),
    pa.field("rawDescription", pa.string()),
    pa.field("verified", pa.bool_()),
    pa.field("created", pa.string()),
    pa.field("followersCount", pa.int64()),
    pa.field("friendsCount", pa.int64()),
    pa.field("statusesCount", pa.int64()),
    pa.field("favouritesCount", pa.int64()),
    pa.field("listedCount", pa.int64()),
    pa.field("mediaCount", pa.int64()),
    pa.field("location", pa.string()),
    pa.field("protected", pa.bool_()),
    pa.field("linkUrl", pa.string()),
    pa.field("linkTcourl", pa.string()),
    pa.field("profileImageUrl", pa.string()),
    pa.field("profileBannerUrl", pa.string()),
    pa.field("url", pa.string())
]

USER_STRUCT = pa.struct(USER_FIELDS)

BASE_SCHEMA = {
    "url": pa.field("url", pa.string()),
    "date": pa.field("date", pa.string()),
    "content": pa.field("content", pa.string()),
    "RenderedContent": pa.field("RenderedContent", pa.string()),
    "id": pa.field("id", pa.int64()),
    "user": pa.field("user", USER_STRUCT),
    "outlinks": pa.field("outlinks", pa.list_(pa.string())),
    "tcooutlinks": pa.field("tcooutlinks", pa.list_(pa.string())),
    "replyCount": pa.field("replyCount", pa.int64()),
    "retweetCount": pa.field("retweetCount", pa.int64()),
    "likeCount": pa.field("likeCount", pa.int64()),
    "quoteCount": pa.field("quoteCount", pa.int64()),
    "conversationId": pa.field("conversationId", pa.int64()),
    "lang": pa.field("lang", pa.string()),
    "mentionedUsers": pa.field("mentionedUsers", pa.list_(USER_STRUCT)),
}