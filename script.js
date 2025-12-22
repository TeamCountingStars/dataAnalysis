// Image data with descriptions
const carouselData = [
    {
        src: "resultsImage/image.png",
        description: "AI 프로젝트 생성량 비교 - 모든 AI 분야에서 2023년 이후 압도적 증가, LLM 분야가 25만 건 이상으로 급부상"
    },
    {
        src: "resultsImage/image-2.png",
        description: "언어별 프로젝트 수 - Python과 Jupyter Notebook이 압도적 1, 2위, JavaScript와 TypeScript의 급격한 증가"
    },
    {
        src: "resultsImage/image-3.png",
        description: "언어별 트렌드 - 2023년 중반 Python이 Jupyter Notebook을 추월, AI 개발 패러다임이 '연구'에서 '실제 애플리케이션 개발'로 전환"
    },
    {
        src: "resultsImage/image-6.png",
        description: "분야별 성장 추이 (Log Scale) - LLM 분야가 2023년 초를 기점으로 수직 상승, 기존 강자를 압도하는 성장률"
    },
    {
        src: "resultsImage/image-7.png",
        description: "LLM 시계열 분해 분석 - 2023년 초를 기점으로 강력한 우상향 추세 시작, 상반기 정점/하반기 저점의 연간 주기 패턴"
    },
    {
        src: "resultsImage/image-9.png",
        description: "Prophet 예측 모델 - 장기 추세와 계절성을 바탕으로 안정적인 미래 예측, ChatGPT/Auto-GPT 이벤트를 특별 이벤트로 분리 학습"
    },
    {
        src: "resultsImage/image-10.png",
        description: "Prophet 모델 분해 분석 - 매끄럽고 강력한 우상향 성장률, 이벤트 제거 후 순수한 12개월 주기 패턴 확인"
    },
    {
        src: "resultsImage/image-11.png",
        description: "분야별 상관관계 분석 - GitHub 프로젝트 증가 시 Stack Overflow 질문은 감소하는 강한 음의 상관관계 발견"
    },
    {
        src: "resultsImage/image-12.png",
        description: "언어별 상관관계 분석 - Python, C++, JavaScript, C# 등 모든 주요 언어에서 강한 음의 상관관계, MATLAB만 예외적으로 양의 상관관계"
    }
];

// Carousel state
let currentIndex = 0;
let rotation = 0;
const totalItems = carouselData.length;
const angleStep = 360 / totalItems;

// Initialize carousel
function initCarousel() {
    const carousel = document.getElementById('carousel');

    carouselData.forEach((data, index) => {
        const item = document.createElement('div');
        item.className = 'carousel-item';

        const img = document.createElement('img');
        img.src = data.src;
        img.alt = `Result ${index + 1}`;

        item.appendChild(img);

        // Calculate position for 3D carousel
        const angle = angleStep * index;
        const radius = 600;
        item.style.transform = `translate(-50%, -50%) rotateY(${angle}deg) translateZ(${radius}px)`;

        carousel.appendChild(item);
    });

    updateDescription();
}

// Update description text
function updateDescription() {
    const descElement = document.getElementById('carouselDesc');
    descElement.textContent = carouselData[currentIndex].description;
}

// Rotate carousel
function rotateCarousel(direction) {
    if (direction === 'next') {
        currentIndex = (currentIndex + 1) % totalItems;
        rotation -= angleStep;
    } else {
        currentIndex = (currentIndex - 1 + totalItems) % totalItems;
        rotation += angleStep;
    }

    const carousel = document.getElementById('carousel');
    carousel.style.transform = `rotateY(${rotation}deg)`;

    updateDescription();
}

// Event listeners
document.getElementById('nextBtn').addEventListener('click', () => {
    rotateCarousel('next');
});

document.getElementById('prevBtn').addEventListener('click', () => {
    rotateCarousel('prev');
});

// Keyboard navigation
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') {
        rotateCarousel('next');
    } else if (e.key === 'ArrowLeft') {
        rotateCarousel('prev');
    }
});

// Initialize on page load
window.addEventListener('DOMContentLoaded', initCarousel);

// Optional: Auto-rotate carousel
let autoRotateInterval;

function startAutoRotate() {
    autoRotateInterval = setInterval(() => {
        rotateCarousel('next');
    }, 5000);
}

function stopAutoRotate() {
    clearInterval(autoRotateInterval);
}

// Uncomment to enable auto-rotation
// startAutoRotate();

// Pause auto-rotation on hover
const carouselContainer = document.querySelector('.carousel-container');
if (carouselContainer) {
    carouselContainer.addEventListener('mouseenter', stopAutoRotate);
    carouselContainer.addEventListener('mouseleave', startAutoRotate);
}
