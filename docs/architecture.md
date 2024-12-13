## Kiến Trúc Hệ Thống

Hệ thống đánh giá này có 5 thành phần chính:

1. **Thu thập dữ liệu**
2. **Xây dựng graph**
3. **Chuyển graph thành embedding**
4. **Gán nhãn chất lượng**
5. **Huấn luyện mô hình (SVM)**

### 1. Lớp Thu Thập Dữ Liệu (Data Collection Layer)

- **Mục tiêu**: Thu thập dữ liệu khóa học từ các nền tảng MOOC.
- **Dữ liệu đầu vào**: Thông tin về khóa học (tên khóa học, mô tả, đánh giá, v.v.), giảng viên, học viên, và các chỉ số khác như tỷ lệ hoàn thành khóa học.

### 2. Lớp Xây Dựng Graph (Graph Construction Layer)

- **Mục tiêu**: Xây dựng một graph mô tả các mối quan hệ giữa các thực thể (khóa học, giảng viên, học viên, đánh giá, v.v.).
- **Công cụ và công nghệ**:
  - **NetworkX**: Thư viện Python giúp xây dựng và xử lý các graph.
  - **Graph structure**:
    - **Đỉnh (nodes)**: Các thực thể như khóa học, giảng viên, học viên, đánh giá.
    - **Cạnh (edges)**: Các mối quan hệ giữa các thực thể, ví dụ: giảng viên dạy khóa học, học viên đánh giá khóa học.

### 3. Lớp Chuyển Graph Thành Embedding (Graph Embedding Layer)

- **Mục tiêu**: Chuyển đổi các đỉnh (nodes) trong graph thành các vector embedding để mô hình học máy có thể sử dụng.
- **Công cụ và công nghệ**:
  - **Node2Vec**: Thuật toán học máy giúp chuyển đổi các nút trong graph thành các vector embedding.
  - Các embedding này đại diện cho các đặc điểm và mối quan hệ giữa các thực thể trong graph.
  
### 4. Lớp Gán Nhãn Chất Lượng (Labeling Layer)

- **Mục tiêu**: Gán nhãn chất lượng cho các khóa học dựa trên các chỉ số và đánh giá.
- **Công cụ và công nghệ**:
  - Các chỉ số đánh giá như: điểm trung bình đánh giá, số lượng học viên đăng ký, tỷ lệ hoàn thành khóa học.
  - **Phân tích cảm xúc** từ nhận xét của học viên để giúp gán nhãn chất lượng (chất lượng cao, trung bình, thấp).
  
### 5. Lớp Huấn Luyện Mô Hình (Model Training Layer)

- **Mục tiêu**: Huấn luyện mô hình học máy (SVM) để dự đoán chất lượng của khóa học dựa trên các embedding và nhãn chất lượng.
- **Công cụ và công nghệ**:
  - **Support Vector Machine (SVM)**: Sử dụng mô hình SVM để phân loại chất lượng khóa học dựa trên các vector embedding.
  - **Scikit-learn**: Thư viện học máy giúp triển khai mô hình SVM.
  - **Dữ liệu huấn luyện**: Sử dụng các embedding từ bước trước và nhãn chất lượng khóa học để huấn luyện mô hình SVM.