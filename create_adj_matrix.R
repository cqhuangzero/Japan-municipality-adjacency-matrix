library(sf)
library(dplyr)
library(spdep)
# library(future.apply)

# You can speed up computing by using more processors, but don't use all
# plan(multisession, workers = 12)

# Read your file
data_origin <- st_read("D:/desktop/map/N03-23_230101.geojson")

# Merge administrative districts
data_origin$N03_004 <- gsub("市.*区$", "市", data_origin$N03_004)

# Merge by prefecture and municipality
data <- data_origin %>%
  group_by(N03_001, N03_004) %>%
  summarise(geometry = st_union(geometry), .groups = "drop")

# Rename columns
colnames(data) <- c("prefecture", "city", "geometry")

# Fix invalid geometries
data$geometry <- st_make_valid(data$geometry)

# Generate nb
nb <- poly2nb(data, queen = T, snap = 0.001)

# Convert to adjacency matrix
adj_matrix <- nb2mat(nb, style = "B", zero.policy = TRUE)

# Save adjacency matrix as CSV
write.csv(adj_matrix, "adj_matrix.csv", row.names = TRUE, fileEncoding = "UTF-8")

