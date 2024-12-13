## Describe

Hệ thống đánh giá chất lượng khóa học sử dụng các phương pháp **graph-based learning** và **machine learning** để dự đoán chất lượng khóa học từ các nền tảng MOOC. Dữ liệu được xây dựng thành một graph, trong đó các khóa học, giảng viên và học viên là các đỉnh (nodes) và các mối quan hệ giữa chúng là các cạnh (edges). Hệ thống sử dụng thuật toán **Node2Vec** để chuyển đổi graph thành các embedding, giúp mô hình học máy có thể phân loại chất lượng khóa học một cách chính xác. Cuối cùng, mô hình **SVM** được huấn luyện để dự đoán chất lượng khóa học dựa trên các embedding và các nhãn chất lượng đã được gán.

## Deployment

Để triển khai hệ thống trên máy tính cá nhân hoặc server, bạn cần đảm bảo các bước sau:

1. **Cài đặt Python**:
   - Hệ thống yêu cầu **Python 3.6**.

2. **Cài đặt các thư viện phụ thuộc**:
   - Sử dụng `pip` để cài đặt tất cả các thư viện cần thiết bằng cách chạy lệnh sau trong terminal:

     ```bash
     pip install -r requirements.txt
     ```

3. **Kiểm tra kết quả**:
   - Sau khi mô hình đã được huấn luyện, bạn có thể sử dụng mô hình để dự đoán chất lượng khóa học bằng cách sử dụng các script dự đoán.

## Dataset

Dữ liệu sử dụng trong hệ thống này được cung cấp từ bộ dữ liệu **MOOCubeX**, có thể tải xuống từ liên kết sau:

- [Tải bộ dữ liệu MOOCCube.zip](http://lfs.aminer.cn/misc/moocdata/data/MOOCCube.zip)

### Mô tả Bộ Dữ Liệu

- **Khóa học**: Tên khóa học, mô tả, thể loại, và các thông tin liên quan khác.
- **Giảng viên**: Thông tin về giảng viên và các khóa học họ giảng dạy.
- **Học viên**: Thông tin về học viên, đánh giá của họ về các khóa học và các hành vi học tập khác.
- **Đánh giá**: Các đánh giá của học viên về khóa học.